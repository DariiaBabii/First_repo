# Створіть функцію get_random_winners(quantity, participants), 
# яка повертатиме список унікальних ідентифікаторів бази даних зі словника participants 
# в кількості quantity. Це буде список переможців

# Вимоги:

# Отримайте перелік ключів словника. 
# (Після виконання методу keys() використовуйте перетворення типів)
# Перемішайте отриманий список за допомогою методу shuffle
# Виберіть випадкових переможців, використовуючи метод sample.
# Якщо передана кількість переможців більша за кількість користувачів 
# (quantity > len(participants)) — поверніть порожній список.

import random


def get_random_winners(quantity, participants):

    if quantity > len(participants):
        return []
    
    list_participants = list(participants.keys())
    random.shuffle(list_participants)
    return random.sample(list_participants, k=quantity)


