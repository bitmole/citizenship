import random

questions = [
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
        'text': 'Who did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": True, 
             "Russia": False,
        },
    },
    {
        'text': 'Who did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": False,
        },
    },
    {
        'text': 'Who did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": False,
        },
    },
    {
        'text': 'Who did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": False,
        },
    },
    {
        'text': 'Who did we fight in war of 1812?',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": False,
        },
    },
]

def ask(q):
    print(q['text'])

    numbered_answers = {str(i):k for i, k in enumerate(q['answers'].keys(), start=1)}

    for i, answer in numbered_answers.items():
        print('%s: %s' % (i, answer))

    return numbered_answers

def correct_answers_to(question):
    return [a for (a, correct) in question['answers'].items() if correct]

def check(answers, question):
    return set(answers) == set(correct_answers_to(question))

def main():

    random.shuffle(questions)

    while questions:
        q = questions.pop()
        options = ask(q)
        selected = input().split(',')
        answers = [v for (k,v) in options.items() if k in selected]

        print('correct' if check(answers, q) else 'wrong')
        print('Correct answer(s):', ' '.join(correct_answers_to(q)))

if __name__ == "__main__":
    main()
