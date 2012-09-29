"""
storygen.py

build a story prompt given some source files.
currently this only works for fables.
"""

import json
import random
import requests
from secrets import usakey


def generate_story(type):
    source_file = open('story_elements.json', 'r')
    my_data = json.load(source_file)
    source_file.close()

    if type == "Fable":
        a = random.choice(my_data['fable_subject'])
        b = random.choice(my_data['fable_body'])
        return "Tell me a fable. How about " + a + " " + b + "?"

    if type == "News":
        req_vars = { 'count':5,
                     'days':0,
                     'page':0,
                     'encoding':'json',
                     'api_key':usakey(),
                   }

        r = requests.get('http://api.usatoday.com/open/articles/topnews/home', params=req_vars)

        articles = r.json
        story_list = articles.get('stories', False)
        if story_list:
            my_story = random.choice(story_list)
            title = my_story.get('title', False)
            if title: 
                link = my_story.get('link', False)
                if link:
                    return "Please comment on the story <a href=" + link + ">" + title + " </a>"
                else:
                    return "Please comment on the story " +  title
            else:
                return "Hey, there was not title to the story"
        else:
            return "Sorry, no news today"

if __name__ == '__main__':
    print generate_story("News")

