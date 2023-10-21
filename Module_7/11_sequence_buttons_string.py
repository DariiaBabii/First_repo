# Напишіть функцію sequence_buttons, що показує послідовність кнопок, 
# яку необхідно натиснути, щоб на екрані телефону з'явився текст, введений користувачем.

# Створіть словник, який відповідає символам з кнопками, які потрібно натиснути.

# Приклад: якщо функції sequence_buttons передати рядок "Hello, World!", 
# функція повинна повернути "4433555555666110966677755531111".

# Вимоги:

# функція коректно обробляє малі та великі літери.
# функція ігнорує символи, що не входять до зазначеного списку


def sequence_buttons(string):
    button_dict = {
        '1': '.,?!:',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ',
        '0': ''
    }
    result = ''
    
    for char in string:
        char_upper = char.upper()
        if char_upper == ' ':
            result += '0'
        for key, value in button_dict.items():
            if char_upper in value:
                repetitions = value.index(char_upper) + 1
                result += key * repetitions

    return result

input_string = "Hi there!"
output = sequence_buttons(input_string)
print(output) 
    
    
        
        
        
