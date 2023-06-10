import json
import datetime

FILE = "notes.json"

def notes_load():
    try:
        with open(FILE, "r", encoding='utf8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def notes_save(notes):
    with open(FILE, "w", encoding='utf8') as file:
        json.dump(notes, file, ensure_ascii=False)

def notes_add():
    title = input("Заголовок: ")
    body = input("Заметка: ")
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    notes_save(notes)
    print("\nЗаметка добавлена")
    
def notes_del():
    note_id = int(input("\nID заметки: "))
    for i, note in enumerate(notes):
        if note["id"] == note_id:
            del notes[i]
            notes_save(notes)
            print("\nЗаметка удалена")
            return
    print("\nЗаметка не найдена")

def notes_list():
    print("")
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Время: {note['timestamp']}")
        
def notes_edit():
    note_id = int(input("ID заметки: "))
    for note in notes:
        if note["id"] == note_id:
            title = input("Новый заголовок (пустой ввод - оставить без изменений): ")
            if title:
                note["title"] = title
            body = input("Новый текст заметки (пустой ввод - оставить без изменений): ")
            if body:
                note["body"] = body
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            notes_save(notes)
            print("\nЗаметка отредактирована")
            return
    print("\nЗаметка не найдена")

notes = notes_load()