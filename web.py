from flask import Flask, url_for, redirect, render_template, abort, request, jsonify

import api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/finish/')
def finish():
    return 'Done!'

@app.route('/random-test.json')
def random_test():
    return jsonify(api.random_test())

@app.route('/questions/<id>/', methods=['POST', 'GET'])
def questions(id):
    try:
        q = api.get_question(id)
    except KeyError:
        abort(404)

    if request.method == 'POST':
        answers = getlist('answers', q, request)
        result, correct, _ = api.check_answers(answers, q)

        return render_template('result.html',
                result=result,
                question=q,
                answers=answers,
                correct=correct)

    return render_template(question_template(q),
            question=q, 
            title=q['text'])

def question_template(q):
    if api.is_freetext(q):
        return 'question-freetext.html'
    elif api.is_multichoice(q):
        return 'question-multichoice.html'
    elif api.is_singlechoice(q):
        return 'question-singlechoice.html'

def getlist(key, q, request):
    if api.is_freetext(q):
        return request.form[key].split(',')
    else:
        return request.form.getlist(key)
