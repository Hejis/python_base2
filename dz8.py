phonebook = {}
def readfile(filename):
    data = [i.split() for i in open(filename, 'r', encoding='utf-8')]
    return data

def printinfo(data):
    for i in data:
        print('выберите пункт меню', i)

data = readfile('tel.txt')

def add_contact(name, number):
    phonebook[name] = number
    print(f"Контакт добавлен.")

def search_contact(name):
    if name in phonebook:
        number = phonebook[name]
        print(f"Номер телефона {name}: {number}")
    else:
        print(f"Контакт не найден.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Контакт удален.")
    else:
        print(f"Контакт не найден.")

def update_contact(name):
    if name in phonebook:
        new_number = input(f"Введите новый номер телефона для контакта {name}: ")
        phonebook[name] = new_number
        print(f"Номер телефона для контакта {name} обновлен.")
    else:
        print(f"Контакт не найден.")

def view_phone_book():
    try:
        with open("tel.txt", "r") as file:
            print("Телефонный справочник:")
            for line in file:
                line = line.strip()
                if line:
                    name, number = line.split(":")
                    print(f"{name}: {number}")
                else:
                    print("Ошибка: некорректная строка в файле справочника.")
    except FileNotFoundError:
        print("Файл справочника не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def main_menu():
    while True:
        print("Телефонный справочник")
        print("1. Добавить контакт")
        print("2. Найти контакт по имени")
        print("3. Удалить контакт")
        print("4. Изменить контакт")
        print("5. Просмотреть весь справочник")
        print("q - Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            number = input("Введите номер телефона: ")
            add_contact(name, number)
        elif choice == "2":
            name = input("Введите имя контакта: ")
            search_contact(name)
        elif choice == "3":
            name = input("Введите имя контакта для удаления: ")
            delete_contact(name)
        elif choice == "4":
            name = input("Введите имя контакта для изменения: ")
            update_contact(name)
        elif choice == "5":
            view_phone_book()
        elif choice == "q":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


main_menu()