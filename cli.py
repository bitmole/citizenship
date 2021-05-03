import random
import api

def present(q):
    assert(q is not None)
    print(q['text'])

    numbered_answers = {str(i):k for i, k in enumerate(q['options'], start=1)}

    for i, answer in numbered_answers.items():
        print('%s: %s' % (i, answer))

    return numbered_answers

def main():
    test = api.random_test()

    while test:
        qid = test.pop()
        question = api.get_question(qid)
        options = present(question)

        answers = input().split(',')
        answers = [v for (k,v) in options.items() if k in answers]

        ok, correct, _ = api.check_answers(answers, question)

        print('correct' if ok else 'wrong')
        print('Correct answer(s):', ', '.join(correct))


if __name__ == "__main__":
    main()
