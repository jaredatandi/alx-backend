#!/usr/bin/env python3
"""
Basic module for flask app
"""

from flask import Flask, render_template, request, session, redirect
from flask_babel import _, Babel
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
babel = Babel(app)


class Config(object):
    """config for babel

    Args:
        object (_type_): _description_
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello_world():
    """Render basic html

    Returns:
        _type_: Rendered file
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
