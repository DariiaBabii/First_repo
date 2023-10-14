from datetime import datetime


def get_str_date(date_str):
    # Конвертуємо рядок у об'єкт datetime
    date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%fZ')
    
    # Повертаємо відформатований рядок дати
    return date_obj.strftime('%A %d %B %Y')

    
    
    
