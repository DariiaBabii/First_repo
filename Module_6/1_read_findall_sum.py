import re
def total_salary(path):
    total_sum = 0
    fh = open(path, 'r')
    lines = fh.readlines()
    for line in lines:
        # Знаходимо всі числа у рядку
        numbers = re.findall(r'[-+]?\d*\.\d+|\d+', line)

        # Додаємо їх до загальної суми
        total_sum += sum(map(float, numbers))
    fh.close()
    return total_sum
    
