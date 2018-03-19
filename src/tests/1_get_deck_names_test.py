import unittest
import os
import sys

from helpers import import_module
lib = import_module('lib', '%s/../1_get_deck_names.py' % os.path.dirname(os.path.realpath(__file__)))

class TestMethods(unittest.TestCase):

    def test_get_deck_names(self):
        self.assertEqual(
            sorted(lib.get_deck_names()),
            ['Default', 'anki-code-second-deck', 'anki-code-test-deck']
        )

if __name__ == '__main__':
    unittest.main()
