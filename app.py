#! /usr/bin/env python

import os
from flask import Flask, flash, render_template

from example import *
from bourbon import *

app = Flask(__name__)

PORT = int(os.environ.get("PORT", '5000'))
DEBUG = os.environ.get('DEBUG', True)
root = Directory(['posts'])
posts = Directory(Post.all())

@app.route('/', methods=['GETATTR'])
def index_getattr():
    return str(root.stat())

@app.route('/', methods=['READDIR'])
def index_readdir():
    return str(root.readdir())

@app.route('/posts', methods=['GETATTR'])
def posts_getattr():
    return str(posts.stat())

@app.route('/posts', methods=['READDIR'])
def posts_readdir():
    return str(posts.readdir())

@app.route('/posts/<post_id>', methods=['GETATTR'])
def post_getattr(post_id):
    return str(Post.stat(post_id))

app.debug = DEBUG
app.run(host='0.0.0.0', port=PORT)
