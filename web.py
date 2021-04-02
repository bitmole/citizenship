from flask import Flask, url_for, redirect, render_template

import api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test/')
def test():
    test = api.random_test()
    first = test.pop()
    # TODO: save rest of test in "session"
    return redirect(url_for('questions', id=first))

@app.route('/questions/<id>/')
def questions(id):
    q = api.get_question(id)
    return render_template('question.html', 
            id=id,
            question=q['text'], 
            answers=q['answers'].keys(),
            title=q['text'])
