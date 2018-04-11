import unittest
import os
import sys

from helpers import import_module
lib = import_module('lib', '%s/../0_create_deck_note_card.py' %
                    os.path.dirname(os.path.realpath(__file__)))

# run `$ ./scripts/copy-profile.sh` after running to restore state


class TestMethods(unittest.TestCase):

    def test_create_deck_note_card(self):
        deck_name = 'test-deck'
        deck = lib.create_deck(deck_name)
        self.assertTrue(deck['id'] > 0)
        self.assertEqual(deck['name'], deck_name)

        note, cards = lib.create_note(deck['id'], 'front', 'back')
        self.assertSequenceEqual(note.fields, ['front', 'back'])
        self.assertTrue(len(cards), 1)


if __name__ == '__main__':
    unittest.main()
