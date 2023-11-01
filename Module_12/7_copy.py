# функція copy_class_person як параметр приймає екземпляр класу person, 
# та повертає "поверхневу" копію об'єкта за допомогою функції copy із пакета copy.

import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)
    