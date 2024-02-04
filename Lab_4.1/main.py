from  pathlib import Path 
import re
import os 


#
def total_salary(path):
    #оголошуємо змінні 
    list_salary = []
    total_salary = None
    average_salary = None

    try:
        
        #Перевіряємо чи присутній файл 
        if os.path.exists(path) :

            #Читаємо файл та присвоюємо його вміст списку lines 
            with open(path, 'r') as salary :
                lines = [el.strip(' ') for el in salary.readlines()]

            #Перевіряємо, чи файл не пустий  та отримуємо тільки заробітні та додаємо їх до списку  list_salary
            if len(lines) > 0 :    
                for i in lines:
                    pattern = r"\d"
                    money = "".join(re.findall(pattern, i))
                    list_salary.append(money)

                #Змінюємо тип  та розраховуємо загальну суму та середнє значення всіх заробініх плат
                list_salary = list(map(int, list_salary))
                total_salary  = sum(list_salary)
                average_salary = int((total_salary) / len(list_salary))

            #Повертаємо значення 
                return total_salary, average_salary
            else:
                print("Перевірте Вміст файлу ")
                return total_salary, average_salary 
        else:
            print("Перевірте наявність файлу")
            return total_salary, average_salary       
    except :
        print("Сталась помилка при виконанні")
        return total_salary, average_salary 

total, average = total_salary("D:\\My_repo\\First_repo\\Lab_4.1\\Salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
