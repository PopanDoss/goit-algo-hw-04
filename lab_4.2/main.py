from  pathlib import Path 
import re

#Створюємо функцію яка буде опрацьовувати файл 
def get_cats_info(path):
    #
    id_info =[]
    name_info = []
    age_info = []

    pets_list = []
    try:
        #створюємо список з рядків в файлі
        with open( path, 'r+') as base:
            raw_list = [el.strip() for el in base.readlines()]
        #перевіряємо. чи файл не пустий 
        if len(raw_list) > 0 :
            #Створюємо список з id кожної тваринки
            for i in raw_list:
                pattern = r"^[^,]+"
                id = "".join(re.findall(pattern, i))
                #перевіряємо чи відповідає id умові
                if len(id) == 24 :
                    id_info.append(id)
                else :
                    return f"Перевірьте правильність вказання id в записі {i}"
            #Створюємо список з імена кожної тваринки, що знаходяться між комами 
            for i in raw_list:
                pattern_2 = r',([^,\s]+),'                            
                name = "".join(re.findall(pattern_2, i))
                #перевіряємо, чи вказане ім"я
                if len(name) > 0 : 
                    name_info.append(name)
                else :
                    return f"Здається, ви не вказали ім\'я котика в записі {i}"
            #Створюємо список для віку котиків, що знаходяться в кінці рядку та мають тільки цифри 
            for i in raw_list :
                pattern_3 = r'[\s,](\d+)$'
                age = "".join(re.findall(pattern_3, i))
                #перевіряємо, чи вказали вік для 
                if len(age) > 0 :
                    age_info.append(age)
                else:
                    return f"здається ви не вказали вік котика в записі {i}" 
            #Створюємо список словників, що складаються з id, імені та віку кожного котика. 
            for i in range(len(id_info)) :
                pets_list.append({"id": id_info[i], "name": name_info[i], "age_info": age_info[i]})
        else :
            return "Перевірте вміст файлу"
        return pets_list
    except: 
        return "Перевірте наявність файлу та шлях до нього" 


cats_info = get_cats_info("D:\\My_repo\\First_repo\\lab_4.2\\base.txt")
print(cats_info)
