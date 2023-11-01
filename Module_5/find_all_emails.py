# використовуємо для email, — англійський алфавіт
# префікс (все, що знаходиться до символу @) починається з латинської літери та може містити будь-яке число або букву, включаючи нижнє підкреслення та символ точки. Має складатися мінімум із двох символів
# суфікс email (все, що знаходиться після символу @) складається лише з букв англійського алфавіту, та має дві частини, розділені точкою, також доменне ім'я верхнього рівня не може бути менш ніж два символи (все, що після точки)


import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-Z][\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
    return result