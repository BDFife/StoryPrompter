"""
StoryPrompter
"""

import os

from flask import Flask
from flask import request
from flask import url_for, redirect
from flask import render_template
from storygen import generate_story

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('prompt.html', story_type="fable", story_string=generate_story())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

