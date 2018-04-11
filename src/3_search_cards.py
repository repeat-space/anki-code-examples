import sys
import os

sys.path.append('%s/../anki' % os.path.dirname(os.path.realpath(__file__)))
from anki import Collection as aopen

# copied from $HOME/.local/share/Anki2/anki-code
path = '%s/data/profile/collection.anki2' % os.getcwd()
collection = aopen(path)


def search_cards(query):
    return collection.findCards(query)


if __name__ == '__main__':
    print(sorted(search_cards('test')))
