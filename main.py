documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_name_by_id(n):
    res = None
    for i in documents:
        if i["number"] == n:
            res = (i["name"])
    return res


def get_shelf_by_n_doc(n):
    res = None
    for k, v in directories.items():
        if n in v:
            res = k
    return res


def print_doc():
    for i in documents:
        print(f'{i["type"]} "{i["number"]}" "{i["name"]}"')
    return


def add_new(n_doc, doc_type, name, n_shelf):
    documents.append({"type": doc_type, "number": n_doc, "name": name})
    if n_shelf not in directories.keys():
        directories[n_shelf] = [n_doc]
    else:
        for k, v in directories.items():
            if k == n_shelf:
                v.append(n_doc)
                break
    return


def get_comand():
    while True:
        comand = input()
        if comand == "p":
            n_doc = input("Введите номер документа! ")
            name = get_name_by_id(n_doc)
            if name != None:
                print(name)
            else:
                print("Нет такого документа!")
        elif comand == "s":
            n_doc = input("Введите номер документа! ")
            n_shelf = get_shelf_by_n_doc(n_doc)
            if n_shelf != None:
                print(n_shelf)
            else:
                print("Нет такого документа на полках!")
        elif comand == "l":
            print_doc()
        elif comand == "a":
            n_doc = input("Введите номер документа ")
            doc_type = input("Введите тип документа ")
            name = input("Введите имя ")
            n_shelf = input("Введите номер полки ")
            add_new(n_doc, doc_type, name, n_shelf)
            print("Информация добавлена!")
        elif comand == "q":
            break
        else:
            print("Введите правильную команду!")


if __name__ == '__main__':
    get_comand()
