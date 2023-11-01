# is_spam_words, яка визначала, чи є чи ні стоп-слова у тексті повідомлення. 
# Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон. 
# Наприклад, всі "погані" слова замінюватимемо зірочками. Напишіть функцію replace_spam_words, 
# яка приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку (параметр spam_words), 
# та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *, причому довжина шаблону дорівнює довжині забороненого слова. 
# Визначити нечутливість до регістру стоп-слів.

import re

def replace_spam_words(text, spam_words):
    # Функція для заміни спам-слова зірочками
    def asterisk_replacer(match):
        return '*' * len(match.group(0))  # створюємо рядок з зірочок довжиною у спам-слово

    for word in spam_words:
        # Замінюємо кожне спам-слово на зірочки з урахуванням регістру
        # re.IGNORECASE допомагає робити пошук без урахування регістру
        # re.escape() - всі спеціальні символи будуть "екрановані", і будуть трактуватися як звичайні символи.
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub(asterisk_replacer, text)

    return text