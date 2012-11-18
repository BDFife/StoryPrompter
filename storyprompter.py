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
	return render_template('story_index.html')

# Defined here to allow a 'back' button in the about page
@app.route('/templates/')
def about():
	return render_template('about.html')

@app.route('/prompt/<type>')
def show_story(type=None):
	if type in genres:
		string = generate_story(type)
	else:
		type = random.choice(genres)
		string = generate_story(type)
	
	return render_template('prompt.html', story_type=type, story_string=string)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
