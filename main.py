import notes_func as nc

while True:
    print("\n1. Добавить\n2. Редактировать\n3. Удалить\n4. Вывести все\n5. Поиск по ID\n6. Поиск по дате\n7. Выход")
    choice = input("\nВыбор: ")
    if choice == "1":
        nc.notes_add()
    elif choice == "2":
        nc.notes_edit()
    elif choice == "3":
        nc.notes_del()
    elif choice == "4":
        nc.notes_list()
    elif choice == "5":
        nc.notes_view()
    elif choice == "6":
        nc.notes_filter_bydate()
    elif choice == "7":
        break
    else:
        print("\nПроверьте правильность ввода")
        
    input("\nНажмите Enter для продолжения")
    