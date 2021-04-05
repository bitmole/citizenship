import random

from utils import slugify, normalize

_questions = [
    {
        'text': 'Who did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": True,
        },
    },
    {
        'text': 'How did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": True, 
             "Russia": False,
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

    if question.get('type', None) == 'freetext':
        if len(submitted) < question.get('min_correct_count', 1):
            return False, correct, incorrect
        else:
            a, b = normalize(submitted, correct)
            return set(a).issubset(set(b)), correct, incorrect

    return set(submitted) == set(correct), correct, incorrect

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
