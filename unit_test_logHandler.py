import unittest
from logHandler import logHandler

output_string = logHandler("input.log")

class LogHandler(unittest.TestCase):
    def test_logHandler(self):
        file = open('output.log', 'r')
        actual_string = file.read()
        file.close()
        self.assertEqual(output_string, actual_string)


if __name__ == '__main__':
    unittest.main()
