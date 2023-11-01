# Нехай є рядок з числами (з метою спрощення числа лише цілі), 
# що визначає якісь частини загального доходу. Наприклад,

# "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
# Необхідно реалізувати функцію generator_numbers, 
# яка буде парсити рядок і знаходити всі цілі числа в ньому та працювати як генератор, 
# який буде віддавати зазначені числа при зверненні до нього у циклі.

# З парсингом рядків ми вже зіштовхувалися виконуючи завдання модуля 7, 
# коли розбивали на лексеми арифметичний вираз

# Функція generator_numbers(string="") безпосередньо розпарсює рядок і за допомогою yield повертає поточне число.

# Функція sum_profit(string) підсумовує числа, отримані від generator_numbers, та повертає загальну суму прибутку з рядка.


import re

def generator_numbers(string=""):
    tokens = re.findall(r"\d+", string)  # Використовуємо регулярний вираз для пошуку чисел в рядку
    numbers = [int(token) for token in tokens]  # Перетворюємо знайдені числа у цілі числа
    yield numbers

def sum_profit(string):
    total = 0
    for numbers in generator_numbers(string):
        total += sum(numbers)  # Сумуємо всі знайдені числа у списку

    return total

# Приклад використання:
input_string = "The price is $15.99, the tax is $2.50, and the total is $18.49"
result = sum_profit(input_string)
print(result)  # Виведе: 18.49

    

print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."))     
    