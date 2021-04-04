from flask import Flask, url_for, redirect, render_template, abort, request

import api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start/')
def start():
    start = api.random_test()
    first = start.pop()
    # TODO: save rest of start in "session"
    return redirect(url_for('questions', id=first))

@app.route('/questions/<id>/', methods=['POST', 'GET'])
def questions(id):
    try:
        q = api.get_question(id)
    except KeyError:
        abort(404)

    if request.method == 'POST':
        answers = request.form['choices'].split() # handle different types
        result, correct, _ = api.check_answers(answers, q)

        #TODO: get next question from session
        return render_template('result.html',
                result=result,
                question=q,
                answers=answers,
                correct=correct,
                next=url_for('questions', id=next_question()))

    return render_template('question.html', 
            question=q, 
            title=q['text'])

def next_question():
    #TODO: get next question from session
    return api.random_test().pop()
