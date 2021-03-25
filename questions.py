import unicodedata
import re
import random

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

def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

def check_answers(answers, question):
    correct = [a for (a, correct) 
            in question['answers'].items() 
            if correct]
    incorrect = [a for (a, correct) 
            in question['answers'].items() 
            if not correct]
    return set(answers) == set(correct), correct, incorrect

def random_quiz():
    ids = list(_questions_dict.keys())
    random.shuffle(ids)
    return ids

def get_question(qid): 
    return _questions_dict[qid]

_questions_dict = {slugify(q['text']):q for q in _questions}