import unittest
import section4_step56


class FizzBuzzTests(unittest.TestCase):
    def test_fizz(self):
        number = 6
        result = section4_step56.get_reply(number)
        self.assertEqual(result, 'Fizz')

    def test_buzz(self):
        number = 10
        result = section4_step56.get_reply(number)
        self.assertEqual(result, 'Buzz')

    def test_fizz_buzz(self):
        number = 15
        result = section4_step56.get_reply(number)
        self.assertEqual(result, 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
