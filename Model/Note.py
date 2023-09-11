from datetime import datetime


class Note:

    def __init__(self, title, text):
        self.date = str(datetime.now().date())
        self.title = title
        self.text = text

    def __str__(self):
        end_text = []
        count = 0
        for i in self.text:
            if i == " " and count >= 40:
                end_text.append("\n")
                count = 0
            else:
                count += 1
                end_text.append(i)
        text = "".join(end_text)
        return f"\nДата создания(редакции) заметки: {self.date}\n" \
               f"Заглавие: {self.title}\n" \
               f"Текст:  {text}\n"

    def change_title(self, new_title):
        self.title = new_title

    def change_text(self, new_text):
        self.text = new_text

    def change_date(self):
        self.date = datetime.now().date()

    def change_note(self, new_title, new_text):
        self.change_title(new_title)
        self.change_text(new_text)
        self.change_date()
