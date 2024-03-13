import csv

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
    """Линейный поиск юзера по айди проекту и возвращаем его данные в формате задания"""
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
def main():
    """
    Точка входа
    """
    header, data = open_csv("../students.csv")
    
    while True:
        inp = input()
        if inp == "СТОП":
            break

        print(linear_search(data, inp))
        
        
        
main()