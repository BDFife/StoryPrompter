"""
storygen.py

build a story prompt given some source files.
currently this only works for fables.
"""

import json
import random
import request

def generate_story(type):
    source_file = open('story_elements.json', 'r')
    my_data = json.load(source_file)
    source_file.close()

    if type == "Fable":
        a = random.choice(my_data['fable_subject'])
        b = random.choice(my_data['fable_body'])
        return "Tell me a story about: " + a + " " + b

    if type == "News":
        
        return "Sorry, no news today"

if __name__ == '__main__':
    print generate_story()

