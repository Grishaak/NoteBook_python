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
                flag = presenter.redact_note(index, new_title, new_text)
                if flag is not None:
                    print_text(flag)
            case "5":
                flag = presenter.save_notes()
                if not flag:
                    print_text("Невозможно сохранить данные.")
            case "6":
                flag = presenter.load_notes()
                if not flag:
                    print_text("Невозможно загрузить файл")
            case "7":
                index = int(scaner(input_index))
                flag = presenter.delete_note(index)
                if flag is not None:
                    print_text(flag)
            case "8":
                break
            case _:
                print_text(error_input)
