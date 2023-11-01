# Приймати список телефонних номерів.
# Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
# Сортувати телефонні номери за вказаними у таблиці країнами.
# Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
# {
#     "UA": [<тут список телефонів>],
#     "JP": [<тут список телефонів>],
#     "TW": [<тут список телефонів>],
#     "SG": [<тут список телефонів>]
# }
# Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    phone_dict = {
        'UA': [],
        'JP': [],
        'TW': [],
        'SG': []
    }

    for phone in list_phones:
        sanitized_phone = sanitize_phone_number(phone)
        if sanitized_phone.startswith("81"):
            phone_dict['JP'].append(sanitized_phone)
        elif sanitized_phone.startswith("65"):
            phone_dict['SG'].append(sanitized_phone)
        elif sanitized_phone.startswith("886"):
            phone_dict['TW'].append(sanitized_phone)
        elif sanitized_phone.startswith("380"):
            phone_dict['UA'].append(sanitized_phone)
        else:
            # Якщо жоден із відомих кодів не зустрічається на початку номера
            phone_dict['UA'].append(sanitized_phone)

    return phone_dict
