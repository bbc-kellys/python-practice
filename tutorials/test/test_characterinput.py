import StringIO
import sys
import unittest
from characterinput.characterinput import printer


class chartests(unittest.TestCase):
    def test(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        printer()
        sys.stdout = sys.__stdout__
        print 'Captured', capturedOutput.getValue()


if __name__ == '__main__':
    unittest.main()
