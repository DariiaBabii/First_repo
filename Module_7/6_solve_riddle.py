# Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) 
# для знаходження слова, що шукається в рядку ребуса.

# Параметри функції:

# riddle - рядок із зашифрованим словом.
# word_length – довжина зашифрованого слова.
# start_letter - літера, з якої починається слово 
# (мається на увазі, що до початку слова літера не зустрічається в рядку).
# reverse - вказує, у якому порядку записане слово. 
# За замовчуванням — в прямому. Для значення True слово зашифроване у зворотньому порядку, 
# наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
# Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.

def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if not reverse:
        for i, letter in enumerate(riddle):
            if letter == start_letter and i + word_length <= len(riddle):
                return riddle[i:i+word_length]
    else:
        for i, letter in enumerate(riddle[::-1]):
            if letter == start_letter and i + word_length <= len(riddle):
                return riddle[-(i+word_length):-i][::-1]
    return ''  # Повернути пустий рядок, якщо не знайдено відповідну послідовність

# Приклад використання:
result = solve_riddle('mi1powperet', 3, 'r', True)
print(result)  # Повинно вивести рядок

            
                
            
                
    