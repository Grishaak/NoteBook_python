import json
from json import JSONEncoder, JSONDecoder

from Model.Note import Note


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

    def from_json(self, json_object):
        if 'title' in json_object:
            x = Note(json_object['title'], json_object["text"], json_object["date"])
            return x

    def encode_to_json(self, notes: dict):
        try:
            with open("file.json", "w") as fp:
                for note in notes.values():
                    product_encoded = json.dumps(note, cls=Encoder)
                    fp.writelines(product_encoded)
                    fp.writelines("\n")
        except IOError:
            raise IOError

    def loads_saves(self):
        try:
            with open(r"file.json", "r") as x:
                lines = sum(1 for line in x)
            data = dict()
            with open(r"file.json", "r") as r:
                for i in range(1, lines + 1):
                    loaded_file = r.readline()
                    note = JSONDecoder(object_hook=self.from_json).decode(loaded_file)
                    data[i] = note
            return data
        except OSError:
            raise OSError
