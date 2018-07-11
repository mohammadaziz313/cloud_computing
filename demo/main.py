from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests
import json
import logging
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

# App config.
DEBUG = True
app = Flask(__name__)



@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/map", methods=['GET','POST'])
def map():
    return render_template('map.html')



if __name__ == '__main__':
    app.run()

