from Model.Exceptions.InvalidIndexError import InvalidIndexError
from Model.NoteBook import NoteBook


class Presenter:
    def __init__(self):
        self.notes = NoteBook()

    def create_note(self, title, text, date):
        self.notes.create_note(title, text, date)

    def show_note(self, index):
        try:
            x = self.notes.show_note(index)
            return x
        except InvalidIndexError as index_error:
            return index_error

    def show_all_notes(self):
        return self.notes.show_all_notes()

    def redact_note(self, index, new_title, new_text):
        try:
            self.notes.redact_note(index, new_title, new_text)
        except InvalidIndexError as index_error:
            return index_error.__str__()

    def show_ids(self):
        return self.notes.show_ids()

    def save_notes(self):
        try:
            self.notes.save_to_json()
        except IOError:
            return False

    def load_notes(self):
        try:
            self.notes.load_saves()
            return True
        except OSError:
            return False

    def delete_note(self, index):
        try:
            self.notes.delete_note(index)
        except InvalidIndexError as e:
            return e

    def sort_by_date(self):
        self.notes.sort_by_date()
