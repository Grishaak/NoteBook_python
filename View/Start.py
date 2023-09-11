from Presenter.Presenter import Presenter
from Texts import *


def start():
    presenter = Presenter()
    while True:
        print_text(menu_text)
        choice = scaner(input_number)
        match choice:
            case "1":
                title = scaner("Введите заглавие: ")
                text = scaner("Введите текст заметки: ")
                presenter.create_note(title, text)
            case "2":
                index = int(scaner(input_index))
                notes = presenter.show_note(index)
                print_text(notes)
            case "3":
                notes = presenter.show_all_notes()
                print_text(notes)
                print_text(presenter.show_ids())
            case "4":
                print_text(presenter.show_ids())
                index = int(scaner(input_index))
                new_title = scaner(input_text)
                new_text = scaner(input_text)
                presenter.redact_note(index, new_title, new_text)
            case "5":
                presenter.save_notes()
            case "6":
                presenter.load_notes()
            case "7":
                index = int(scaner(input_index))
                presenter.delete_note(index)
            case "8":
                break
            case _:
                print_text(error_input)
