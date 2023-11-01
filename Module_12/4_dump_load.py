# Розробіть клас Person. Він має чотири властивості: ім'я користувача name, його email, 
# телефонний номер phone та властивість favorite - обраний контакт чи ні.

# Приклад створення екземпляра класу:

#     Person(
#     "Allen Raymond",
#     "nulla.ante@vestibul.co.uk",
#     "(992) 914-3792",
#     False,
# )
# Розробіть клас Contacts. Він повинен ініціалізувати через конструктор дві властивості: 
# filename - ім'я файлу для пакування об'єкта класу Contacts, contacts - список контактів, 
# екземплярів класу Person.

# Приклад створення екземпляра класу:

# contacts = [
#     Person(
#         "Allen Raymond",
#         "nulla.ante@vestibul.co.uk",
#         "(992) 914-3792",
#         False,
#     ),
#     Person(
#         "Chaim Lewis",
#         "dui.in@egetlacus.ca",
#         "(294) 840-6685",
#         False,
#     ),
# ]

# persons = Contacts("user_class.dat", contacts)
# Розробіть два методи для серіалізації та десеріалізації екземпляра класу Contacts за допомогою пакету pickle
# та зберігання даних у бінарному файлі.

# Перший метод save_to_file зберігає екземпляр класу Contacts у файл, використовуючи метод dump пакету pickle. 
# Ім'я файлу зберігається в атрибуті filename.

# Другий метод read_from_file читає та повертає екземпляр класу Contacts з файлу filename, використовуючи метод load пакету pickle.

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite
        
        


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.save_to_file()
        self.read_from_file()
        
        

    def save_to_file(self):
        with open(self.filename, 'wb') as fn:
            pickle.dump(self, fn)
        
            

    def read_from_file(self):
        with open(self.filename, 'rb') as fn:
            content = pickle.load(fn)
        return content

            
        