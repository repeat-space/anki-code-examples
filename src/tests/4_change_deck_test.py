import unittest
import os
import sys

from helpers import import_module
lib = import_module('lib', '%s/../4_change_deck.py' %
                    os.path.dirname(os.path.realpath(__file__)))

# run `$ ./scripts/copy-profile.sh` after running to restore state


class TestMethods(unittest.TestCase):

    def test_change_deck(self):
        search_results = lib.search_cards('*')
        self.assertEqual(len(search_results), 2)

        deck_name_source = 'anki-code-test-deck'
        deck_name_target = 'anki-code-second-deck'
        search_results = lib.search_cards('deck:%s' % deck_name_target)
        self.assertEqual(len(search_results), 1)
        search_results = lib.search_cards('deck:%s' % deck_name_source)
        self.assertEqual(len(search_results), 1)

        card_id = search_results[0]
        card = lib.collection.getCard(card_id)
        deck_source_id = lib.collection.decks.id(deck_name_source)
        deck_target_id = lib.collection.decks.id(deck_name_target)
        self.assertEqual(card.did, deck_source_id)
        self.assertNotEqual(deck_source_id, deck_target_id)

        lib.change_deck([card_id], deck_target_id)

        search_results = lib.search_cards('deck:%s' % deck_name_target)
        self.assertEqual(len(search_results), 2)
        search_results = lib.search_cards('deck:%s' % deck_name_source)
        self.assertEqual(len(search_results), 0)

        lib.collection.save()
        lib.collection.close(save=False)


if __name__ == '__main__':
    unittest.main()
