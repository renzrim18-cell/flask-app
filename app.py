from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

@app.route('/info')
def info():
    return 'Flask läuft in Docker | Python Version: ' + __import__('sys').version

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
