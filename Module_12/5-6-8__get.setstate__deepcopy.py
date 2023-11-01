# Додайте до класу Contacts атрибут count_save, за замовчуванням він повинен мати значення 0. 
# Реалізуйте магічний метод __getstate__ для класу Contacts. 
# При упаковуванні екземпляра метод класу повинен збільшувати значення атрибута count_save на одиницю. 
# Таким чином, ця властивість - лічильник повторних операцій пакування екземпляра класу

import pickle
import copy


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
        self.count_save = 0
        self.is_unpacking = False
        

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes
        
# Додайте до класу Contacts атрибут is_unpacking, за замовчуванням він повинен мати значення False. 
# Реалізуйте магічний метод __setstate__ для класу Contacts. 
# При розпаковуванні екземпляра класу метод повинен змінювати значення атрибута is_unpacking на значення True. 
# Таким чином, ця властивість визначатиме, що екземпляр класу отримано внаслідок розпакування.        

    def __setstate__(self, value):
        self.__dict__.update(value)
        self.is_unpacking = True

# для класу Contacts створення поверхневої копії екземпляра класу не увінчається успіхом через те, 
# що ми маємо атрибут contacts, який є списком екземплярів об'єктів класу Person, 
# а отже, всі вони будуть передані за посиланням. 
# Тому необхідно використовувати глибоке копіювання методом deepcopy з пакета copy

    def copy_class_contacts(contacts):
        return copy.deepcopy(contacts)




        