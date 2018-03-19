import sys
import os

sys.path.append('%s/../anki' % os.path.dirname(os.path.realpath(__file__)))
from anki import Collection as aopen


def get_cards_from_deck(deck_name):
    # copied from $HOME/.local/share/Anki2/anki-code
    path = '%s/data/profile/collection.anki2' % os.getcwd()
    collection = aopen(path)  # linux

    deck_id = collection.decks.id(deck_name)
    collection.decks.select(deck_id)

    card = collection.sched.getCard()  # next in schedule
    note = card.note()

    return {
        'card': card,
        'note': note,
    }


if __name__ == '__main__':
    print(sorted(get_cards_from_deck('anki-code-second-deck')))
