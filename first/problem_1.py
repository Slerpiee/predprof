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


def main():
    """
    Точка входа
    """
    header, data = open_csv("../students.csv")
    counter, s = 0, 0
    for user in data:
        try:
            score = int(user["score"])
            counter += 1
            s += score
        except:
            continue
    sr_zn = s/counter
    rounded = round(sr_zn, 3)
    for user in data:
        try:
            int(user["score"]) 
        except:
            user["score"] = str(rounded)
    write_csv("student_new.csv", header, data)
    for user in data:
        if "Хадаров Владимир" in user["Name"]:
            print(f"Ты получил {user['score']} за проект {user['titleProject_id']}")
            break

main()