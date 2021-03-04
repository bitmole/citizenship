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
    answers = {i:(k,v) for i, (k,v) in enumerate(q['answers'].items(), start=1)}
    for k, v in answers.items():
        answer, _ = v
        print('%d: %s' % (k, answer))
    return answers

def main():
    for q in questions:
        answers = ask(q)
        a = int(input())
        print('Answered:', answers[a])
        print('Correct:', [a for (a, correct) in answers.values() if correct])
        


if __name__ == "__main__":
    main()
