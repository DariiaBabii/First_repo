# Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, 
# де ключ це IP, а значення – кількість входжень у вказаний список.
# Друга функція get_frequent_visit_from_ip повертає кортеж 
# з найбільш часто уживаним в списку IP і кількістю його появ в списку.

from collections import Counter

def get_count_visits_from_ip(ips):
    ips_count = Counter(ips)
    return ips_count

def get_frequent_visit_from_ip(ips):
    frequent_ip = get_count_visits_from_ip(ips)
    return frequent_ip.most_common(1)[0]
# метод .most_common(1) повертає список з одним кортежем. 
# Щоб отримати сам кортеж, ми використовуємо індексацію [0] 
    