import random

questions = [
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

    numbered_answers = {i:k for i, k in enumerate(q['answers'].keys(), start=1)}

    for i, answer in numbered_answers.items():
        print('%d: %s' % (i, answer))

    return numbered_answers

def correct_answers_to(question):
    return [a for (a, correct) in question['answers'].items() if correct]

def check(answer, question):
    return answer in correct_answers_to(question)
    # TODO: use set comparison to support multiple choice or text input

def main():

    random.shuffle(questions)

    while questions:
        q = questions.pop()
        numbered_answers = ask(q)
        i = int(input())
        a = numbered_answers[i]

        print('%s is %s' % (a, 'correct' if check(a, q) else 'wrong'))
        print('Correct answer:', ' '.join(correct_answers_to(q)))

if __name__ == "__main__":
    main()
