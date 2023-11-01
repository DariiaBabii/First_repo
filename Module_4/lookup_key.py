# lookup_key для пошуку всіх ключів за значенням у словнику. Першим параметром у функцію ми передаємо словник, 
# а другим — значення, що хочемо знайти. 
# Таким чином, результат може бути як список ключів, так і порожній список, якщо ми нічого не знайдемо.

def lookup_key(data, value_to_find):
    matching_keys = []
    for l, current_value in data.items():
        if value_to_find == current_value:
            matching_keys.append(l)
    return matching_keys
