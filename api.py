import random

from utils import slugify, normalize

_questions = [
    {
        'text': 'What is the supreme law of the land?',
        'answers': {
             "the Declaration of Independence": False,
             "the Constitution": True,
             "the Common Law": False, 
             "the Bible": False,
        },
    },
    {
        'text': 'What does the Constitution do?',
        'answers': {
             "Sets up the government": True,
             "Defines the government": True,
             "Protects basic rights of Americans": True, 
             "Specifies the ruling party": False,
        },
    },
    {
        'text': 'When did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": False,
        },
    },
    {
        'text': 'Why did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": False,
        },
        'type': 'freetext'
    },
    {
        'text': 'What did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": False,
        },
    },
    {
        'text': 'Whom did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": False,
        },
    },
]

_questions_dict = {slugify(q['text']):q for q in _questions}

def check_answers(submitted, question):
    correct = [a for (a, correct) 
            in question['answers'].items() 
            if correct]
    incorrect = [a for (a, correct) 
            in question['answers'].items() 
            if not correct]

    submitted, correct = normalize(submitted, correct)
    submitted, correct = set(submitted), set(correct)
    
    if is_freetext(question):
        has_min_correct_count = len(submitted) >= question.get('min_correct_count', 1)
        result = has_min_correct_count and submitted.issubset(correct)
    else: # question type is a choice
        result = submitted == correct

    return result, correct, incorrect

def random_test():
    ids = list(_questions_dict.keys())
    random.shuffle(ids)
    return ids

def get_question(qid): 
    return _questions_dict[qid]

def is_freetext(q):
    return q.get('type', None) == 'freetext'

def is_multichoice(q):
    correct = [a for (a, correct) 
            in q['answers'].items() 
            if correct]
    return len(correct) > 1

def is_singlechoice(q):
    correct = [a for (a, correct) 
            in q['answers'].items() 
            if correct]
    return len(correct) == 1
