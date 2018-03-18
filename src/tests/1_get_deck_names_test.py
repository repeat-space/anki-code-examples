import unittest
import os
import sys
import importlib.util

lib_path = "%s/../1_get_deck_names.py" % os.path.dirname(os.path.realpath(__file__))
spec = importlib.util.spec_from_file_location('lib', lib_path)
lib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lib)

class TestMethods(unittest.TestCase):

    def test_get_deck_names(self):
        self.assertEqual(
            sorted(lib.get_deck_names()),
            ['Default', 'anki-code-second-deck', 'anki-code-test-deck']
        )

if __name__ == '__main__':
    unittest.main()
