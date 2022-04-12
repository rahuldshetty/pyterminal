import pty, subprocess, shlex, select, os, struct, fcntl, termios

from flask import render_template
from pyterminal.extension import app, socket_io
from pyterminal.parser import parser
from pyterminal.utility import logger

@app.route('/')
def hello():
    return render_template('index.html')

def set_window_size(fd, row,col, xpix=0, ypix=0):
    winsize = struct.pack("HHHH", row, col, xpix, ypix)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, winsize)

def read_and_forward_pty_output():
    max_read_bytes = 1024*20
    while True:
        socket_io.sleep(0.01)
        if app.config["fd"]:
            timeout_sec = 0
            (data_ready, _, _) = select.select([app.config["fd"]],[],[], timeout_sec)
            if data_ready:
                output = os.read(app.config['fd'], max_read_bytes).decode()
                socket_io.emit("pty-output", {"output": output}, namespace="/conn")


@socket_io.on("pty-input", namespace="/conn")
def pty_input(data):
    """ 
    Write to child pty
    """
    if app.config["fd"]:
        os.write(app.config["fd"], data["input"].encode())


@socket_io.on('connect', namespace="/conn")
def connect():
    """
    New Client is connected
    """

    # Already started child process, do not start new process
    if app.config["child_pid"]:
        return
    
    # Create a child process attached to a pty on which we can write
    (child_pid, fd) = pty.fork()
    
    if child_pid == 0:
        # First child fork
        # output of this will be presented in pty
        subprocess.run(app.config["cmd"])
    else:
        # parent process fork
        # store child fd and pid
        logger.info("Child pid: %s", child_pid)
        app.config["fd"] = fd 
        app.config["child_pid"] = child_pid
        set_window_size(fd, 50, 50)
        cmd = " ".join(shlex.quote(c) for c in app.config["cmd"])
        logger.info("Starting background task with command to read/write to/from client and pty")
        socket_io.start_background_task(
            target=read_and_forward_pty_output
        )
        logger.info("Session started.")

@socket_io.on("resize", namespace="/conn")
def resize(data):
    if app.config["fd"]:
        set_window_size(app.config["fd"], data["rows"], data["cols"])

def main():
    '''
    Application Entrypoint.
    '''
    args = parser()
    cmd = [args.cmd] +  shlex.split(args.args)
    logger.info("Launching PyTerminal with cmd/args: %s", cmd)
    logger.info("Running PyTerminal server at %s:%s", args.host, args.port)
    app.config["cmd"] = cmd
    
    socket_io.run(app, debug=args.debug, port=args.port, host=args.host)

if __name__ == '__main__':
    main()