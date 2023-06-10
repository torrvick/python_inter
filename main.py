import notes_func as nc

while True:
    print("\n1. Добавить\n2. Редактировать\n3. Удалить\n4. Вывести все\n5. Поиск по ID\n6. Поиск по дате\n7. Выход")
    choice = input("Выбор: ")
    if choice == "1":
        nc.notes_add()
    # elif choice == "2":
    #     edit_note()
    elif choice == "3":
        nc.notes_del()
    elif choice == "4":
        nc.notes_list()
    # elif choice == "5":
    #     view_note()
    # elif choice == "6":
    #     filter_notes()
    elif choice == "7":
        break
    else:
        print("\nПроверьте правильность ввода")
        
    input("\nНажмите Enter для продолжения")
    