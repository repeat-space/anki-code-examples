import unittest
import os
import sys

from helpers import import_module
lib = import_module('lib', '%s/../3_search_cards.py' %
                    os.path.dirname(os.path.realpath(__file__)))


class TestMethods(unittest.TestCase):

    def test_search_cards(self):
        # https://apps.ankiweb.net/docs/manual.html#searching
        self.assertSequenceEqual(lib.search_cards(
            '*'), [1521410434570, 1521410453807])
        self.assertSequenceEqual(lib.search_cards('test'), [1521410453807])
        self.assertSequenceEqual(lib.search_cards(
            'deck:anki-code-second-deck'), [1521410434570])

        deck_name = 'anki-code-second-deck'
        card_by_deck_id = lib.search_cards('deck:%s' % deck_name)[0]
        card_by_deck = lib.collection.getCard(card_by_deck_id)
        deck_id = lib.collection.decks.id(deck_name)
        self.assertEqual(card_by_deck.did, deck_id)


if __name__ == '__main__':
    unittest.main()
