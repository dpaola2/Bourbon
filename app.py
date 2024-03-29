#! /usr/bin/env python

import os
from flask import Flask, flash, render_template

from example import *
from bourbon import *
import json

app = Flask(__name__)

PORT = int(os.environ.get("PORT", '5000'))
DEBUG = os.environ.get('DEBUG', True)

@app.route('/', methods=['GETATTR'])
def index_getattr():
    return json.dumps(root.stat())

@app.route('/', methods=['READDIR'])
def index_readdir():
    return str(root.readdir())

@app.route('/posts', methods=['GETATTR'])
def posts_getattr():
    return json.dumps(posts.stat())

@app.route('/posts', methods=['READDIR'])
def posts_readdir():
    return str(posts.readdir())

@app.route('/posts/<post_id>', methods=['GETATTR'])
def post_getattr(post_id):
    return json.dumps(Post.stat(post_id))

@app.route('/posts/<post_id>', methods=['READ'])
def post_read(post_id):
    p = Post.open(post_id)
    data = p.read()
    p.close()
    return str(data)

app.debug = DEBUG
app.run(host='0.0.0.0', port=PORT)
