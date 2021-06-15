from shlex import split

from pyterminal.extension import app
from pyterminal.parser import parser
from pyterminal.utility import logger

@app.route('/')
def hello():
    return 'Hello World!'

def main():
    '''
    Application Entrypoint.
    '''
    args = parser()
    cmd = [args.cmd] +  split(args.args)
    logger.info("Launching PyTerminal with cmd/args: %s", cmd)
    logger.info("Running PyTerminal server at %s:%s", args.host, args.port)


if __name__ == '__main__':
    main()