from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, This is DaEun Kim.'


@app.route('/info')
def info():
    return 'Info'
