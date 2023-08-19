# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой).
import json
import os
from datetime import datetime

notes_file = "notes.json"

def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            return json.load(file)
    else:
        return []

def save_notes(notes):
    with open(notes_file, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def display_notes(notes_list=None):
    if not notes_list:
        notes_list = notes
    print("Заметки:")
    print("=" * 30)
    for note in notes_list:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['body']}")
        print(f"Дата/время: {note['timestamp']}")
        print("=" * 30)

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое тело заметки: ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            break
    else:
        print("Заметка с указанным ID не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            break
    else:
        print("Заметка с указанным ID не найдена")

def filter_by_date():
    date_string = input("Введите дату (ГГГГ-ММ-ДД), для которой хотите увидеть заметки: ")
    filtered_notes = [note for note in notes if note["timestamp"].startswith(date_string)]
    if filtered_notes:
        display_notes(filtered_notes)
    else:
        print("Заметки для указанной даты не найдены")

notes = load_notes()

while True:
    print("Введите команду: \nadd - добавить заметку, \nlist - показать все заметки, \nview - просмотреть заметку, \nedit - редактировать заметку, \ndelete - удалить заметку, \nfilter - фильтр по дате, \nexit - выход")
    command = input()
    
    if command == "add":
        add_note()
    elif command == "list":
        display_notes()
    elif command == "view":
        note_id = int(input("Введите ID заметки для просмотра: "))
        for note in notes:
            if note["id"] == note_id:
                display_notes([note])
                break
        else:
            print("Заметка с указанным ID не найдена")
    elif command == "edit":
        edit_note()
    elif command == "delete":
        delete_note()
    elif command == "filter":
        filter_by_date()
    elif command == "exit":
        break
    else:
        print("Неверная команда. Пожалуйста, выберите из списка.")