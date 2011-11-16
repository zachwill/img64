"""
Taken from:  https://gist.github.com/1094140
"""

from functools import wraps
from flask import request, current_app


def jsonp(function):
    """Wraps JSONified output for JSONP requests."""
    @wraps(function)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(function(*args,**kwargs).data) + ')'
            return current_app.response_class(content, mimetype='application/javascript')
        else:
            return function(*args, **kwargs)
    return decorated_function
