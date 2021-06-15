from pyterminal.extension import app
from pyterminal.parser import parser

@app.route('/')
def hello():
    return 'Hello World!'

def main():
    '''
    Application Entrypoint.
    '''
    args = parser()

if __name__ == '__main__':
    main()