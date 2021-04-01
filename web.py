from flask import Flask, url_for, redirect

import api

app = Flask(__name__)

@app.route('/')
def start():
    test = api.random_test()
    first = test.pop()
    # TODO: save rest of test in "session"
    return redirect(url_for('question', id=first))

@app.route('/question/<id>/')
def question(id):
    q = api.get_question(id)
    return _present(q)

def _present(question):
    # TODO: generate dynamic web form
    return question['text']

