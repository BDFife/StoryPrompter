"""
StoryPrompter
"""

import os
import random

from flask import Flask
from flask import request
from flask import url_for, redirect
from flask import render_template
from storygen import generate_story

genres = ["Fable", "Fable", "News", "Personal", "Personal"]

app = Flask (__name__)

@app.route('/')
def index():
    my_genre = random.choice(genres)
    return render_template('prompt.html', story_type=my_genre, story_string=generate_story(my_genre))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

