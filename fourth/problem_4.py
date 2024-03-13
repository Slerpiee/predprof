import csv
import string
import random
import sys


def open_csv(filename):
    """Функция парсит файл, возвращает его первую строчку и данные
    
    Параметры:
    filename - путь открываемого файла
    
    """
    head = []
    data = []
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        isHeader = True
        for obj in reader:
            if isHeader:
                head = obj
                isHeader = False
                continue
            user = {}
            for ind_parsed in range(0, len(obj)):
                user[head[ind_parsed]] = obj[ind_parsed] 
            data.append(user)
    return head, data
   


def write_csv(filename, header, data):
    """
    Записывает дату в csv фай
    
    Параметры:
    header - первая строчка для разметки файла
    data - список с пользователями
    filename - путь к записываемому файлу
    """ 
    
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        clear_data = []
        for pole in data:
            d = pole.values()
            clear_data.append(d)
        for row in clear_data:
            writer.writerow(row)

def ins_sort(users, key):
    """
    Сортируем вставками и возвращаем отсортированный список пользователей на основе ключ_функции

    Параметры:
    users - массив словарей пользователей
    key - ключ функция 
    """
    data = [key(i) for i in users]
    


    for i in range(0, len(data)):
        j = i - 1 
        key = data[i]
        u_key = users[i]
        while data[j] >= key and j >= 0:
            data[j + 1] = data[j]
            users[j+1] = users[j]
            j -= 1
        data[j + 1] = key
        users[j+1] = u_key


def linear_search(data, id):
    """
    Линейный поиск юзера по айди проекту и возвращаем его данные в формате задания
    Параметры:
    data - список пользователей
    id  - айди проекта
    """
    res = None
    for user in data:
        if user["titleProject_id"] == id:
            res = user
            break
    if res is not None:
        name_data = res["Name"].split()
        n = name_data[1][0]
        s_n = name_data[0]
        return f"Проект No {id} делал: {n}. {s_n} он(а) получил(а) оценку - {user['score']}"
    return "Ничего не найдено"


def generate_login(name_data):
    """Функция генерирует логин по имени
    Параметры:
    name_data - name пользователь
     """
    name_data = name_data.split()
    s_n = name_data[0]
    n1, n2 = name_data[1][0], name_data[2][0]
    return f"{s_n}_{n1+n2}"

def generate_password():
    """Генерируем пароль"""
    uppper = string.ascii_uppercase
    lower = string.ascii_lowercase
    password = ""
    for i in range(8):
        if random.randrange(0, 2):
            if random.randrange(0,2):
                password += uppper[random.randrange(0, len(uppper)-1)]
            else:
                password += lower[random.randrange(0, len(lower)-1)]
        else:
            password += str(random.randrange(0, 10))
    return password


def main():
    """
    Точка входа
    """
    
    data = sys.stdin.read()
    with open("students_password.csv", "w") as f:
        f.write(data)
    header, data = open_csv("students_password.csv")
    header.append("login")
    header.append("data")
    for user in data:
        user["login"] = generate_login(user["Name"])
        user["passowrd"] = generate_password()
    write_csv("students_password.csv", header, data)

    
    # header.append("login")
    # header.append("password")
    
    
        
    
        
        
main()