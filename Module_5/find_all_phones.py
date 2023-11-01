# використовуємо тільки цифри та символи +, (, ) та -
# телефонний номер починається із символу +
# шаблон телефону символ + потім три цифри 380, символ (, дві цифри, символ ), три цифри, символ -, одна або дві цифри, символ -, дві чи три цифри
# Довжина шаблону телефонного номера завжди 17 символів

import re


def find_all_phones(text):
    result = re.findall(r"\+380\(\d{2}\)\d{3}-\d-\d{3}|\+380\(\d{2}\)\d{3}-\d{2}-\d{2}", text)
    return result