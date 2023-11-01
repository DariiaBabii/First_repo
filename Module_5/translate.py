# За допомогою функції zip, за аналогією прикладу теорії, створіть словник TRANS для транслітерації. 
# Створюйте словник TRANS поза функцією translate

# Напишіть функцію translate, яка проводить транслітерацію кириличного алфавіту на латинську.

# Функція translate:

# приймає на вхід рядок та повертає рядок;
# проводить транслітерацію кириличних символів на латиницю;

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
    

def translate(name):
    translated_name = ""
    for i in name:
        translated_name += TRANS.get(ord(i), i) 
    return translated_name
