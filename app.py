# https://flask.palletsprojects.com/en/2.1.x/quickstart/
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'
