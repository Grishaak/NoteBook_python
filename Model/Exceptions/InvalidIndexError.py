class InvalidIndexError(Exception):
    def __init__(self, text_error):
        self.text_error = text_error

    def __str__(self):
        return f"Ошибка {type(self).__name__}. " \
               f"{self.text_error}\n"
