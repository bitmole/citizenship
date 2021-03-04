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
]

def ask(q):
    print(q['text'])

    all_answers = {i:(k,v) for i, (k,v) in enumerate(q['answers'].items(), start=1)}
    correct_answers = [a for (a, correct) in all_answers.values() if correct]

    for k, v in all_answers.items():
        answer, _ = v
        print('%d: %s' % (k, answer))

    return all_answers, correct_answers

def correct(answers):
    return [a for (a, correct) in answers.values() if correct]

def main():
    for q in questions:
        all_answers, correct_answers = ask(q)
        a = int(input())
        answered, _ = all_answers[a]
        print('Answered:', answered)
        print('Correct:', correct_answers)
        print('Correct!' if answered in correct_answers else 'Wrong...')
        


if __name__ == "__main__":
    main()
