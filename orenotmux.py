#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

# Create application
app = Flask(__name__)
#app.config.from_object(__name__)
#app.config.from_envvar('CUBJECTIVES_SETTINGS', silent=True)


# Routing
# 1) Main page.
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# 2) Hello page.
@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run()
