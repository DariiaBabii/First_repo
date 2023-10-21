# Створіть функцію get_employees_by_profession(path, profession). 
# Функція повинна у файлі (параметр path) знайти всіх співробітників зазначеної професії 
# (параметр profession)

# Вимоги:

# відкрийте файл за допомогою with для читання
# отримайте рядки з файлу за допомогою методу readlines()
# за допомогою методу find знайдіть усі рядки у файлі, де є вказана profession, 
# та помістіть записи до списку
# об'єднайте всі ці рядки в списку в один рядок за допомогою методу join 
# (пам'ятайте про символ перенесення рядків '\n' та зайві прогалини, які треба прибрати)
# приберіть значення змінної 'profession' (замініть на порожній рядок "" методом replace)
# поверніть отриманий рядок із файлу

def get_employees_by_profession(path, profession):
    with open(path, 'r') as fh:
        lines = fh.readlines()

    employees = []

    for line in lines:
        if profession in line:
            # Розділімо рядок на слова та відфільтруємо лише ті, які не є професією
            words = [word for word in line.split() if word != profession]
            employees.extend(words)

    # Повернемо імена, розділені пробілом
    return ' '.join(employees)



        
    
    
        
            
    
    
