import unittest
from io import StringIO
import sys

def process_rage_message(message):
    unique_chars = set()
    rage_message = {}
    current_char_set = ''
    index = 0
    current_num = ''
    while index < len(message):
        if message[index].isdigit():
            while index < len(message) and message[index].isdigit():
                current_num += message[index]
                index += 1
            rage_message[current_char_set] = int(current_num)
            current_char_set = ''
            current_num = ''
        else:
            unique_chars.add(message[index].upper())
            current_char_set += message[index].upper()
            index += 1

    return unique_chars, rage_message

class TestRageMessage(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdout = self.held

    def test_basic_rage_message(self):
        message = "a3BC2"
        unique_chars, rage_message = process_rage_message(message)
        self.assertEqual(len(unique_chars), 3)
        self.assertEqual(rage_message, {'A': 3, 'BC': 2})
        print(f'Unique symbols used: {len(unique_chars)}')
        print(''.join([chars * nums for chars, nums in rage_message.items()]))
        self.assertEqual(sys.stdout.getvalue().strip(), 'Unique symbols used: 3\nAAABCBC')

    def test_complex_rage_message(self):
        message = "aSd2&5s@1"
        unique_chars, rage_message = process_rage_message(message)
        self.assertEqual(len(unique_chars), 5)
        self.assertEqual(rage_message, {'ASD': 2, '&': 5, 'S@': 1})
        print(f'Unique symbols used: {len(unique_chars)}')
        print(''.join([chars * nums for chars, nums in rage_message.items()]))
        self.assertEqual(sys.stdout.getvalue().strip(), 'Unique symbols used: 5\nASDASDASDASDASDASDS@')



    def test_repeated_chars(self):
        message = "aaa2AAA3"
        unique_chars, rage_message = process_rage_message(message)
        self.assertEqual(len(unique_chars), 1)
        self.assertEqual(rage_message, {'AAA': 2, 'AAA': 3})
        print(f'Unique symbols used: {len(unique_chars)}')
        print(''.join([chars * nums for chars, nums in rage_message.items()]))
        self.assertEqual(sys.stdout.getvalue().strip(), 'Unique symbols used: 1\nAAAAAAAAAA')

    def test_empty_input(self):
        message = ""
        unique_chars, rage_message = process_rage_message(message)
        self.assertEqual(len(unique_chars), 0)
        self.assertEqual(rage_message, {})
        print(f'Unique symbols used: {len(unique_chars)}')
        print(''.join([chars * nums for chars, nums in rage_message.items()]))
        self.assertEqual(sys.stdout.getvalue().strip(), 'Unique symbols used: 0\n')

if __name__ == '__main__':
    unittest.main()