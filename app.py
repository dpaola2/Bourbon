#! /usr/bin/env python

import os
from flask import Flask, flash, render_template

app = Flask(__name__)

PORT = int(os.environ.get("PORT", '5000'))
DEBUG = os.environ.get('DEBUG', True)

@app.route('/')
def index():
    "Hello, world"

app.debug = DEBUG
app.run(host='0.0.0.0', port=PORT)
