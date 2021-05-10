import random

from utils import slugify, normalize

_questions = [
    {
        'text': 'What is the supreme law of the land?',
        'correct': [
            'The Constitution',
        ],
        'incorrect': [
             "the Declaration of Independence",
             "the Constitution",
             "the Common Law",
             "the Bible",
        ],
    },
    {
        'text': 'What does the Constitution do?',
        'correct': [
             "Sets up the government",
             "Defines the government",
             "Protects basic rights of Americans",
        ],
        'incorrect': [
             "Specifies the ruling party",
        ],
    },
    {
        'text': 'When did we fight in war of 1812?',
        'correct': [
             "England",
        ],
        'incorrect': [
             "France",
             "Spain",
             "Russia",
        ],
    },
    {
        'text': 'Name one native American tribe',
        'correct': [
            'Ute', 
            'Navajo', 
            'Sioux', 
            'Apache', 
            'Cherokee',
        ],
        'choice': False
    },
]

_questions_dict = {slugify(q['text']):q for q in _questions}

def correct_answers_to(q):
    return q.get('correct', [])

def incorrect_answers_to(q):
    return q.get('incorrect', [])

def check_answers(submitted, question):
    submitted, correct = normalize(submitted, correct_answers_to(question))
    submitted, correct = set(submitted), set(correct)
    
    if is_freetext(question):
        has_min_correct_count = len(submitted) >= question.get('min_correct_count', 1)
        result = has_min_correct_count and submitted.issubset(correct)
    else: # question type is a choice
        result = submitted == correct

    return result, correct_answers_to(question), incorrect_answers_to(question)

def random_test():
    ids = list(_questions_dict.keys())
    random.shuffle(ids)
    return ids

def get_question(qid): 
    q = _questions_dict[qid]
    q['options'] = get_options(q)
    return q

def get_options(question, shuffled=True):
    options = correct_answers_to(question) + incorrect_answers_to(question)
    if shuffled: 
        random.shuffle(options)
    return options

def is_choice(q):
    return q.get('choice', True)

def is_multichoice(q):
    return is_choice(q) and len(correct_answers_to(q)) > 1

def is_singlechoice(q):
    return is_choice(q) and len(correct_answers_to(q)) == 1

def is_freetext(q):
    return not is_choice(q)
