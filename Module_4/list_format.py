# format_ingredients прийматиме на вхід список з інгредієнтів ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] 
# та повертатиме рядок зібраний з його елементів в описаний вище спосіб. 
# Ваша функція має вміти обробляти списки будь-якої довжини.


def format_ingredients(items):
     if not items:
        return ""
     elif len(items) == 1:
        return items[0]
    # Якщо в списку два елементи
     elif len(items) == 2:
        return " and ".join(items)
    # Для списків із більше ніж двома елементами
     else:
        return ", ".join(items[:-1]) + " and " + items[-1]