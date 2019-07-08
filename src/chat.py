# -*- coding: utf-8 -*-

"""A chat/shoutbox using Sijax."""

import os
import hmac
from hashlib import sha1
import flask

from flask import Flask, g, render_template, abort, request, jsonify
from flask import session as f_session
from werkzeug.security import safe_str_cmp
import flask_sijax

# dependencies and prerequisites
import nltk
import pickle
import fileinput
import numpy as np
import pandas as pd
import os, re, math
import tensorflow as tf

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app = Flask(__name__)

app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)


def init():
    # a function to initialise model
    # include all functions to initialise your chatbot in the init() function in the app.py
    return

def get_response():
    # a function to get the response
    # include all functions to get response in the get_response() function in the app.py
    return



@app.route("/api/response")
def response():

    global personality

    requested_personality = request.args.get('personality')
    requested_personality = str(requested_personality).lower()
    personality = requested_personality

    message = request.args.get('message')
    message = str(message)

    bot_response = get_response(message)

    info = {
       "personality" : personality,
       "input" : message,
       "msg" : bot_response
    }
    return jsonify(info)

@app.route('/')
def index():
    return render_template('chat.html')


if __name__ == '__main__':
    init()
    app.run(debug=True, port=8080, host='0.0.0.0')
