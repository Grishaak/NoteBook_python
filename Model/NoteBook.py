from Model.Note import Note
from Model.Encoder import Encoder


class NoteBook:
    def __init__(self):
        self.notes = dict()
        self.index = 0
        self.encoder = Encoder()

    def __str__(self):
        string = ''
        for index, note in self.notes.items():
            string += "\nid заметки: " + str(index)
            string += str(note) + "\n"
        return string

    def create_note(self, title, text):
        note = Note(title, text)
        self.index += 1
        record = self.notes
        record[self.index] = note

    def redact_note(self, index, new_title, new_text):
        note = self.notes.get(index)
        note.change_note(new_title, new_text)

    def show_all_notes(self):
        return self.__show_all_notes()

    def show_note(self, index):
        return self.notes.get(index)

    def __show_all_notes(self):
        return self.__str__()

    def show_ids(self):
        string = "ids: ["
        for index in self.notes.keys():
            string += str(index) + " "
        string += "]"
        return string

    def save_to_json(self):
        data = self.notes
        self.encoder.encode_to_json(data)

    def load_saves(self):
        loaded_data = self.encoder.loads_saves()
        self.notes = loaded_data
        self.index = len(loaded_data.keys())
