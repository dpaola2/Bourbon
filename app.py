#! /usr/bin/env python

import os
from flask import Flask, flash, render_template

from example import *
from bourbon import *

app = Flask(__name__)

PORT = int(os.environ.get("PORT", '5000'))
DEBUG = os.environ.get('DEBUG', True)
root = Directory(['posts'])

@app.route('/', methods=['GETATTR'])
def index_getattr():
    return str(root.stat())

@app.route('/', methods=['READDIR'])
def index_readdir():
    return str(root.readdir())

app.debug = DEBUG
app.run(host='0.0.0.0', port=PORT)
