#!/usr/bin/env python3

from flask import Flask, render_template

from core.controllers.books import controller as books


omnibus = Flask(__name__)
omnibus.register_blueprint(books)


# TODO 1    Write the logic to create a key that be used to will sign cookies.


# def keymaker(omnibus, filename='secret_key'): # TODO 1
#    pass                                       # TODO 1
# keymaker(omnibus)                             # TODO 1

@omnibus.route('/', methods=['GET'])
def home():
    return render_template('index.html')
