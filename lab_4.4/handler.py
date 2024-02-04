


#функція, що зчитує команду та значення
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#функція, що додає новий запис в список 
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts :
        contacts[name] = phone
        return "Contact added."
    else :
        return "Contact already exists"

#функція, що змінює запис в списку
def  change_contact(args, contacts):
    name, phone = args
    if name in contacts :
        contacts[name] = (phone)
        return "Contact updated."
    else:
        return f"Contact {name} not found"

#функція, що відображає номер контакту     
def show_phone(args, contacts) :
    name = args[0] 
    if name in contacts :
        return contacts[name]
    else:
        return f"Contact {name} not found"

#функція, що відображає всі записи в словнику 
def show_all(contacts):
    if len(contacts)>0 :
        return contacts
    else: 
        return "Сontact list is empty"


     

