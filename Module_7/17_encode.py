# Напишіть рекурсивну функцію encode для кодування списку або рядка. 
# Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) 
# або рядок (наприклад, "XXXZZXXYYYZZ"). Функція повинна повернути закодований список елементів 
# (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).

def encode(data):
    if not data:
        return []

    def recursive_encode(data, current_char, count, result):
        if not data:
            result.append(current_char)
            result.append(count)
            return result

        first_char = data[0]

        if first_char == current_char:
            return recursive_encode(data[1:], current_char, count + 1, result)
        else:
            result.append(current_char)
            result.append(count)
            return recursive_encode(data[1:], first_char, 1, result)

    return recursive_encode(data[1:], data[0], 1, [])

# Приклади використання:
data1 = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
result1 = encode(data1)
print(result1)  # Виведе: ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]

data2 = "XXXZZXXYYYZZ"
result2 = encode(list(data2))
print(result2)  # Виведе: ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]







