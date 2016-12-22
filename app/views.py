from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }

    ]

    characters = [
        {
            'name': 'miguel',
            'stats': [{'name': 'strength', 'value': '5'},
                     {'name': 'magic', 'value': '6'}]
        },
        {
            'name': 'andrea',
            'stats': [{'name': 'strength', 'value': '2'},
                     {'name': 'magic', 'value': '8'}]
        },
    ]
    return render_template("index.html",
                           title='Home',
                           characters=characters)


