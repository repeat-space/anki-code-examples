import sys
import os
import tempfile

sys.path.append('%s/../anki' % os.path.dirname(os.path.realpath(__file__)))
from anki import Collection as aopen
from anki.notes import Note

path = '%s/collection.anki2' % tempfile.mkdtemp()
collection = aopen(path)


def create_deck(name):
    deck_id = collection.decks.id(name)
    return collection.decks.get(deck_id)


def create_note(deck_id, front, back):
    # anki/tests/test_schedv2.py
    collection.decks.select(deck_id)
    note = collection.newNote()
    note['Front'] = front
    note['Back'] = back
    collection.addNote(note)  # added_cards_count

    note = collection.getNote(note.id)
    cards = note.cards()

    return note, cards


if __name__ == '__main__':
    print(sorted(search_cards('test')))
