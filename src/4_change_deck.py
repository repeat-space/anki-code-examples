import sys
import os

sys.path.append('%s/../anki' % os.path.dirname(os.path.realpath(__file__)))
from anki import Collection as aopen
from anki.utils import ids2str, intTime

# copied from $HOME/.local/share/Anki2/anki-code
path = '%s/data/profile/collection.anki2' % os.getcwd()
collection = aopen(path)


def search_cards(query):
    return collection.findCards(query)

# from anki/aqt/browser.py _setDeck


def change_deck(cards_ids, deck_id):
    mod = intTime()
    usn = collection.usn()

    cards_ids_str = ids2str(cards_ids)
    collection.sched.remFromDyn(cards_ids)

    # then move into new deck
    collection.db.execute("""
update cards set usn=?, mod=?, did=? where id in """ + cards_ids_str,
                          usn, mod, deck_id)


if __name__ == '__main__':
    print(sorted(search_cards('test')))
