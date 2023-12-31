#!/usr/bin/env python3
"""
Basic module for flask app
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Render basic html

    Returns:
        _type_: Rendered file
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
