import unittest
from io import StringIO
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    def runTest(self, expected_out, given_answer=None):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            import ex1_0
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def test(self):
        self.runTest("hi!\nthis is another message 😅\nhi john!")


if __name__ == '__main__':
    unittest.main()
