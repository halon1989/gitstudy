from flask import Flask

from app import app


@app.route('/index')
def index():
    return 'index'



