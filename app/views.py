"""
Flask Blueprint Docs:  http://flask.pocoo.org/docs/api/#flask.Blueprint

This file is used for both the routing and logic of your
application.
"""

import base64
from urllib import unquote
from urllib2 import urlopen

from flask import Blueprint, render_template, request, jsonify
from utils import jsonp

views = Blueprint('views', __name__, static_folder='../static',
                  template_folder='../templates')


@views.route('/')
@jsonp
def home():
    """Render website's home page or encode the requested image."""
    query = request.args.get('q')
    if query:
        return json_encode(unquote(query))
    return render_template('home.html')


def json_encode(image):
    """Return a JSON response of the base64 encoded image."""
    data = encode(image)
    return jsonify({'data': data})


def encode(image):
    """Base64 encode an external image resource."""
    request = urlopen(image)
    size = request.headers.get('Content-Length')
    if int(size) > 900000:
        return 'That image is way too big.'
    encoding = request.headers.get('Content-Type').replace(' ', '')
    data_type = "data:%s;base64," % encoding
    data = base64.encodestring(request.read()).replace('\n', '')
    return data_type + data


# The functions below should be applicable to all Flask apps.

@views.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return views.send_static_file(file_dot_text)


@views.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
