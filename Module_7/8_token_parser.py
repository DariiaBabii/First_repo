# В арифметичному виразі лексемами є: оператори, числа та дужки. 
# Операторами у нас будуть такі символи: *, /, - та +. 
# Оператори та дужки легко виділити у рядку — вони складаються з одного символу 
# і ніколи не є частиною інших лексем. Числа виділити складніше, 
# оскільки ці лексеми можуть складатися з кількох символів. 
# Тому будь-яка безперервна послідовність цифр — це одна числова лексема.

# Напишіть функцію, яка приймає параметр рядок, що містить математичний вираз, 
# і перетворює його в список лексем. Кожна лексема має бути або оператором, або числом, або дужкою.

import re
def token_parser(s):
    tokens = re.findall(r"\w+|\W", s)
    while ' ' in tokens:
        tokens.remove(' ')

    return tokens

print(token_parser("2+ 34-5 * 3"))