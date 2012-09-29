"""
storygen.py

build a story prompt given some source files.
currently this only works for fables.
"""

import json
import random

def generate_story():
    source_file = open('story_elements.json', 'r')
    my_data = json.load(source_file)
    source_file.close()

    a = random.choice(my_data['fable_subject'])
    b = random.choice(my_data['fable_body'])

    return a + " " + b

if __name__ == '__main__':
    print generate_story()
