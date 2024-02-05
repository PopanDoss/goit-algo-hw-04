from  pathlib import Path
import os 

def get_cats_info(path):
    
    cat_list = [] 
    
    try:
        #Перевіряємо шлях до файлу 
        if os.path.exists(path):
        
            with open( path, 'r+') as base:
                raw_list = [el.strip() for el in base.readlines()]

            #перевіряємо чи файл пустий 
            if len(raw_list) > 0:
            
                #Створюємо список словників з даних в файлі
                for i in raw_list:
                    cat = i.split(',') 
                    cat_list.append({'id': cat[0], 'name': cat[1], 'age': cat[2]})

                return cat_list
            else:
                return 'Перевірте всім файлу'
        else:
            return 'Перевірте шлях до файлу'
    except:
        print('Виникла помилка')
    
        


cats_info = get_cats_info("D:/My_repo/First_repo/lab_4.2/base.txt")
print(cats_info)