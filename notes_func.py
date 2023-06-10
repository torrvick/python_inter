import json
import datetime

FILE = "notes.json"

def notes_load():
    try:
        with open(FILE, "r") as file:
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
    
notes = notes_load()