import os

from flask import Flask

flask_app = Flask(__name__, root_path=os.path.dirname(os.path.dirname(__file__)))

@flask_app.route('/')
def index():
    return 'Hello, This is DaEun Kim.'

@flask_app.route('/info')
def info():
    return 'Info'
