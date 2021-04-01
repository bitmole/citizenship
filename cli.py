import random
import unittest
import api


class CitizenshipTest(unittest.TestCase):
    q = { 'text': 'Question with 2 correct options',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": True,
        },
    }

    q_free_text = { 
        'text': 'Name one American Indian tribe in the United States.',
        'type': 'free_text',
        'min_correct_count': 1,
        'answers': {
             "Cherokee": True,
             "Navajo": True,
             "Sioux": True, 
             "Chippewa": True,
        },
    }

    def test_check_complete_answer(self):
        answers = ['England', 'Russia']
        ok, _, _ = api.check_answers(answers, self.q)
        self.assertTrue(ok)

    def test_check_complete_answer_different_order(self):
        answers = ['Russia', 'England']
        ok, _, _ = api.check_answers(answers, self.q)
        self.assertTrue(ok)

    def test_check_incomplete_answer(self):
        answers = ['England']
        ok, _, _ = api.check_answers(answers, self.q)
        self.assertFalse(ok)

    def test_check_wrong_answer(self):
        answers = ['Spain']
        ok, _, _ = api.check_answers(answers, self.q)
        self.assertFalse(ok)

    def test_check_invalid_answer(self):
        answers = ['Foo']
        ok, _, _ = api.check_answers(answers, self.q)
        self.assertFalse(ok)

    def test_check_empty_answer(self):
        answers = []
        ok, _, _ = api.check_answers(answers, self.q)
        self.assertFalse(ok)

    def test_check_free_text_answer_correct(self):
        answers = ['Navajo', 'Sioux']
        ok, _, _ = api.check_answers(answers, self.q_free_text)
        self.assertTrue(ok)

    def test_check_free_text_answer_incorrect(self):
        answers = ['foo', 'bar']
        ok, _, _ = api.check_answers(answers, self.q_free_text)
        self.assertFalse(ok)

    def test_check_free_text_answer_incomplete(self):
        answers = []
        ok, _, _ = api.check_answers(answers, self.q_free_text)
        self.assertFalse(ok)

    def test_check_free_text_answer_correct_mixed_case(self):
        answers = ['naVajo', 'SIOuX']
        ok, _, _ = api.check_answers(answers, self.q_free_text)
        self.assertTrue(ok)

    def test_check_free_text_answer_correct_extra_spaces(self):
        answers = ['   Navajo   ', '  Sioux         ']
        ok, _, _ = api.check_answers(answers, self.q_free_text)
        self.assertTrue(ok)


def present(q):
    print(q['text'])

    numbered_answers = {str(i):k for i, k in enumerate(q['answers'].keys(), start=1)}

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
        if question.get('type', None) != 'options':
            answers = [v for (k,v) in options.items() if k in answers]

        ok, correct, _ = api.check_answers(answers, question)

        print('correct' if ok else 'wrong')
        print('Correct answer(s):', ', '.join(correct))


if __name__ == "__main__":
    # main()
    unittest.main()
