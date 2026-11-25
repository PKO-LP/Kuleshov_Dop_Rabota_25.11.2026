books = 0

while True:
    print()
    print("Меню:")
    print("1 - Выдать книгу")
    print("2 - Показать количество выданных книг")
    print("3 - Сбросить счетчик")
    print("4 - Вернуть книгу")
    print("0 - Выход")
    
    choice = input("Введите команду: ")
    
    if choice == "1":
        books = books + 1
        print("Книга выдана.")
    elif choice == "2":
        print("Сейчас выдано книг:", books)
    elif choice == "3":
        books = 0
        print("Счетчик сброшен до 0.")
    elif choice == "4":
        if books == 0:
            print("Нет выданных книг")
        else:
            books = books - 1
            print("Книга возвращена.")
    elif choice == "0":
        print("Выход из программы.")
        break
    else:
        print("Неизвестная команда")
