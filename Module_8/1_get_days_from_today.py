from datetime import datetime

def get_days_from_today(date):
    # Розбиваємо вхідний рядок на рік, місяць та день за допомогою циклу for
    date_parts = date.split('-')
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    
    # Створюємо об'єкт datetime для вхідної дати
    input_date = datetime(year, month, day).date()  # Використовуємо .date(), щоб отримати лише дату без часу
    
    # Отримуємо поточну дату (без часу)
    today = datetime.today().date()
    
    # Обчислюємо різницю між датами
    delta = today - input_date
    
    # Повертаємо кількість днів
    return delta.days

# Приклад використання:
print(get_days_from_today("2021-10-09"))  # Наприклад, для 5 травня 2021 це поверне -157
