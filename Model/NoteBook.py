from Model.Note import Note
from Model.Encoder import Encoder
from Model.Exceptions.InvalidIndexError import InvalidIndexError


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

    def create_note(self, title: str, text, date):
        title, text = self.__test_title_text(title, text)
        note = Note(title, text, date)
        self.index += 1
        record = self.notes
        record[self.index] = note

    def redact_note(self, index, new_title, new_text):
        new_title, new_text = self.__test_title_text(new_title, new_text)
        if index not in self.notes.keys():
            raise InvalidIndexError("Записи по такому индексу не найдено.")
        note = self.notes.get(index)
        note.change_note(new_title, new_text)

    def delete_note(self, index):
        if index not in self.notes.keys():
            raise InvalidIndexError("Записи по такому индексу не найдено.")
        self.notes.pop(index)

    def show_all_notes(self):
        return self.__show_all_notes()

    def show_note(self, index):
        if index not in self.notes.keys():
            raise InvalidIndexError("Записи по такому индексу не найдено.")
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
        try:
            data = self.notes
            self.encoder.encode_to_json(data)
        except IOError:
            raise IOError

    def load_saves(self):
        try:
            loaded_data = self.encoder.loads_saves()
            self.notes = loaded_data
            self.index = len(loaded_data.keys())
        except OSError:
            raise OSError

    def __test_title_text(self, title, text):
        if title == "":
            title = "< Без оглавления. >"
        if text == "":
            text = "< Без текста. >"
        return title, text

    def sort_by_date(self):
        # import operator
        new_sorted_dict = {}
        for i, value in sorted(self.notes.items(), key=lambda note: note[1].date, reverse=False):
            new_sorted_dict[i] = value
        self.notes = new_sorted_dict
