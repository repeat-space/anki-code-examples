import sys
import os

sys.path.append('%s/../anki' % os.path.dirname(os.path.realpath(__file__)))
from anki import Collection as aopen

def get_deck_names():
    # copied from $HOME/.local/share/Anki2/anki-code
    path = '%s/data/profile/collection.anki2' % os.getcwd()
    collection = aopen(path)  # linux

    return list(map(lambda deck: deck['name'], collection.decks.all()))

if __name__ == '__main__':
    print(sorted(get_deck_names()))
