"""
format_elements.py

take a bunch of flat text files and json-ify them for usage with storygen.py
"""

import json

def get_file_data(file_name):
    file_obj = open(file_name, 'r')
    file_lines = file_obj.readlines()
    # fixme: adds empty lines as written
    file_lines = map(lambda s:s.strip(), file_lines)
    file_obj.close()
    return file_lines

source_data = {}
source_names = ['fable_subject', 'fable_body']

for item in source_names:
    item_data = get_file_data(item + '.txt')
    source_data[item] = item_data

element_file = open('story_elements.json', 'w')
json.dump(source_data, element_file, indent=4)
element_file.close()

