import os

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def search_name(doc_num, documents):
    for doc in documents:
        if doc['number'] == doc_num:
            return doc['name']


def search_place(doc_num, directories):
    for dir in directories:
        if doc_num in directories.get(dir):
            return dir


def print_list(documents):
    if len(documents) > 0:
        for doc in documents:
            print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')
    else:
        print('Доументов нет')


def add_doc(doc_type, doc_num, own_name, num_dir, documents, directories):
    if num_dir not in directories:
        return False

    directories[num_dir].append(doc_num)
    documents.append({'type': doc_type, 'number': doc_num, 'name': own_name})
    return True


def del_doc(doc_num, documents, directories):
    for dir in directories:
        if doc_num in directories.get(dir):
            directories[dir].remove(doc_num)

            for doc in documents:
                if doc_num == doc.get('number'):
                    documents.remove(doc)
                    return True

    return False


def move_doc(doc_num, num_dir, documents, directories):
    if num_dir in directories:
        for dir in directories:
            if doc_num in directories[dir]:
                directories[dir].remove(doc_num)
                directories[num_dir].append(doc_num)
                return num_dir
        return ('num_error')
    else:
        return 'dir_error'


def add_dir(num_dir, directories):
    if num_dir in directories:
        return False

    directories.update({num_dir: []})
    return True


def main():
    while True:
        print('Для поиска ФИО по номеру документа введите "p"')
        print('Для поиска размещения документа полке по номеру введите "s"')
        print('Для вывода всех документов введите "l"')
        print('Для добавления документа введите "a"')
        print('Для удаления документа введите "d"')
        print('Для перемещения документа на другую полку введите "m"')
        print('Для добавления полки введите "as"')
        print('Для выхода из программы введите "e"')
        print()
        command = input("Введите команду: ")

        if command == 'p':
            cls()
            num = input('Введите номер документа и нажмите "Ввод": ')
            cls()
            res = search_name(num, documents)
            if res is not None:
                print(f' Владелец: {res}')
            else:
                print('Документ не найден')

            print()
            input('Для продолжения нажмимте "Ввод"')
            cls()

        elif command == 's':
            cls()
            num = input('Введите номер документа и нажмите "Ввод": ')
            cls()
            res = search_place(num, directories)
            if res is not None:
                print(f' Документ находится на полке: {res}')
            else:
                print('Документ не найден')

            print()
            input('Для продолжения нажмимте "Ввод"')
            cls()

        elif command == 'l':
            cls()
            print_list(documents)
            print()
            input('Для продолжения нажмимте "Ввод"')

            cls()

        elif command == 'a':
            cls()
            doc_type = input('Введите тип документа и нажмите "Ввод": ')
            doc_num = input('Введите номер документа и нажмите "Ввод": ')
            own_name = input('Введите имя владельца и нажмите "Ввод": ')
            num_dir = input('Введите номер полки и нажмите "Ввод": ')
            cls()

            if add_doc(doc_type, doc_num, own_name, num_dir, documents, directories) is True:
                print(f'Документ успешно добавлен на полку № {num_dir}')
            else:
                print('Ошибка добавления документа. Полки не существует!')

            print()
            input('Для продолжения нажмимте "Ввод"')
            cls()

        elif command == 'd':
            cls()
            num = input('Введите номер документа и нажмите "Ввод": ')

            if del_doc(num, documents, directories) is True:
                print(f'Документ № {num} успешно удален')
            else:
                print('Ошибка удаления. Документ не существует!')

            print()
            input('Для продолжения нажмимте "Ввод"')
            cls()

        elif command == 'm':
            cls()

            doc_num = input('Введите номер документа и нажмите "Ввод": ')
            num_dir = input('Введите номер целевой полки и нажмите "Ввод": ')
            cls()
            res = move_doc(doc_num, num_dir, documents, directories)

            if res == 'num_error':
                print('Документа не существует')
            elif res == 'dir_error':
                print('Целевой полки не существует')
            else:
                print(f'Документ № {doc_num} перемещен на полку № {res}')

            print()
            input('Для продолжения нажмимте "Ввод"')
            cls()

        elif command == 'as':
            cls()
            num_dir = input('Введите номер полки и нажмите ввод: ')

            if add_dir(num_dir, directories):
                print(f'Полка № {num_dir} успешно добавлена')
            else:
                print('Полка уже существует')

            print()
            input('Для продолжения нажмимте "Ввод"')
            cls()



        elif command == 'e':
            cls()
            print('Bye)')
            return

        else:
            cls()
            input('Команда не распознана, нажмите "Ввод"')
            cls()


if __name__ == '__main__':
    main()
