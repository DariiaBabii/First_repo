# створення декоратора для функції sanitize_phone_number. 
# Декоратор повинен додавати для коротких номерів префікс +38, 
# а для повного міжнародного номера (з 12 символом) - тільки знак +. 
# Реалізуйте декоратор format_phone_number для функції sanitize_phone_number з необхідним функціоналом.

def format_phone_number(func):
    def wrapper(phone):
        new_phone = func(phone)
        if len(new_phone) == 10:
            return f"+38{new_phone}"
        elif len(new_phone) == 12:
            return f"+{new_phone}"
        return new_phone
    return wrapper
           


@format_phone_number
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


print(sanitize_phone_number("38(050)123-32-34"))