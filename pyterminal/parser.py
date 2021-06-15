import argparse
import pyterminal.constants as cn

__verion__ = cn.VERSION

def parser():
    parser = argparse.ArgumentParser(
        description="Launch a local terminal in your browser.",
        formatter_class=argparse.HelpFormatter
    )
    parser.add_argument("-p", "--port", default=cn.DEFAULT_PORT, help="Port on which application is exposed.")
    parser.add_argument("--host", default=cn.DEFAULT_HOST, help="Host address to run the server.")
    parser.add_argument("-d" ,"--debug", action="store_true", help="Run server in Debug Mode.")
    parser.add_argument("-v", "--version", action="store_true", help="pyterminal version.")
    parser.add_argument(
        "-c" ,"--cmd", default="bash", help="Command to run in the terminal"
    )
    parser.add_argument(
        "-a",
        "--args",
        default="",
        help="arguments to pass to command (i.e. --args='arg1 arg2 --flag')",
    )
    args = parser.parse_args()
    if args.version:
        print(__verion__)
        exit(0)
    return args
    
    