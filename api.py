import random
import unittest
import questions


def ask(q):
    print(q['text'])

    numbered_answers = {str(i):k for i, k in enumerate(q['answers'].keys(), start=1)}

    for i, answer in numbered_answers.items():
        print('%s: %s' % (i, answer))

    return numbered_answers


class CitizenshipTest(unittest.TestCase):
    q = { 'text': 'Question with 2 correct options',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": True,
        },
    }

    def test_check_complete_answer(self):
        answers = ['England', 'Russia']
        ok, _, _ = questions.check_answers(answers, self.q)
        self.assertTrue(ok)

    def test_check_complete_answer_different_order(self):
        answers = ['Russia', 'England']
        ok, _, _ = questions.check_answers(answers, self.q)
        self.assertTrue(ok)

    def test_check_incomplete_answer(self):
        answers = ['England']
        ok, _, _ = questions.check_answers(answers, self.q)
        self.assertFalse(ok)

    def test_check_wrong_answer(self):
        answers = ['Spain']
        ok, _, _ = questions.check_answers(answers, self.q)
        self.assertFalse(ok)

    def test_check_invalid_answer(self):
        answers = ['Foo']
        ok, _, _ = questions.check_answers(answers, self.q)
        self.assertFalse(ok)

    def test_check_empty_answer(self):
        answers = []
        ok, _, _ = questions.check_answers(answers, self.q)
        self.assertFalse(ok)


def main():
    test = questions.random_quiz()

    while test:
        qid = test.pop()
        question = questions.get_question(qid)
        options = ask(question)
        selected = input().split(',')
        answers = [v for (k,v) in options.items() if k in selected]

        ok, correct, _ = questions.check_answers(answers, question)

        print('correct' if ok else 'wrong')
        print('Correct answer(s):', ', '.join(correct))


if __name__ == "__main__":
    unittest.main()
    main()
