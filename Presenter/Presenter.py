from Model.NoteBook import NoteBook


class Presenter:
    def __init__(self):
        self.notes = NoteBook()

    def create_note(self, title, text):
        self.notes.create_note(title, text)

    def show_note(self, index):
        return self.notes.show_note(index)

    def show_all_notes(self):
        return self.notes.show_all_notes()

    def redact_note(self, index, new_title, new_text):
        self.notes.redact_note(index, new_title, new_text)

    def show_ids(self):
        return self.notes.show_ids()

    def save_notes(self):
        self.notes.save_to_json()

    def load_notes(self):
        self.notes.load_saves()

    def delete_note(self, index):
        self.notes.delete_note(index)
