import random
import unittest
import questions

def ask(q):
    print(q['text'])

    numbered_answers = {str(i):k for i, k in enumerate(q['answers'].keys(), start=1)}

    for i, answer in numbered_answers.items():
        print('%s: %s' % (i, answer))

    return numbered_answers

def check(answers, question):
    return set(answers) == set(correct_answers_to(question))

def correct_answers_to(question):
    return [a for (a, correct) in question['answers'].items() if correct]

def main():
    random.shuffle(questions)

    while questions:
        q = questions.pop()
        options = ask(q)
        selected = input().split(',')
        answers = [v for (k,v) in options.items() if k in selected]

        print('correct' if check(answers, q) else 'wrong')
        print('Correct answer(s):', ' '.join(correct_answers_to(q)))

class CitizenshipTest(unittest.TestCase):

    q = {
        'text': 'Question with 2 correct options',
        'answers': {
             "France": False,
             "England": True,
             "Spain": False, 
             "Russia": True,
        },
    }
    
    def test_check_complete_answer(self):
        answers = ['England', 'Russia']
        self.assertTrue(check(answers, self.q))

    def test_check_complete_answer_different_order(self):
        answers = ['Russia', 'England']
        self.assertTrue(check(answers, self.q))

    def test_check_incomplete_answer(self):
        answers = ['England']
        self.assertFalse(check(answers, self.q))

    def test_check_wrong_answer(self):
        answers = ['Spain']
        self.assertFalse(check(answers, self.q))

    def test_check_invalid_answer(self):
        answers = ['Foo']
        self.assertFalse(check(answers, self.q))

    def test_check_empty_answer(self):
        answers = []
        self.assertFalse(check(answers, self.q))

if __name__ == "__main__":
    # main()
    unittest.main()
