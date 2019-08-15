import sys
import unittest
from characterinput import characterinput

class TestCharInput(unittest.TestCase):
    def test(self):
        self.assertEqual(characterinput())


if __name__ == '__main__':
    unittest.main()