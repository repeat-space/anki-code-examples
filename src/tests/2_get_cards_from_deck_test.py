import unittest
import os
import sys

from helpers import import_module
lib = import_module('lib', '%s/../2_get_cards_from_deck.py' %
                    os.path.dirname(os.path.realpath(__file__)))


class TestMethods(unittest.TestCase):

    def test_get_deck_names(self):
        deck_name = 'anki-code-second-deck'

        ret = lib.get_cards_from_deck('anki-code-second-deck')
        self.assertEqual(sorted(list(ret.keys())), ['card', 'note'])

        self.assertDictEqual(
            ret['card']._getQA(False, False),
            {'a': 'card-1\n\n<hr id=answer>\n\nback-1',
                'id': 1521410434570, 'q': 'card-1'}
        )
        self.assertSequenceEqual(ret['note'].tags, [])
        self.assertEqual(ret['note'].model()['type'], 0)


if __name__ == '__main__':
    unittest.main()
