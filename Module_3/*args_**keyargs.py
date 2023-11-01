# перша first буде мати першим параметром змінну size, а також вона може приймати будь-яку кількість позиційних аргументів. 
# Функція повинна повернути суму size із загальною кількістю переданих до неї позиційних аргументів.
# друга функція second так само матиме першим параметром size і прийматиме довільну кількість ключових аргументів, 
# і також має повернути суму size з кількістю переданих у функцію ключових аргументів.

# def first(size, *arg):
#     return size + len(arg)

# def second(size, **key_arg):
#     return size + len(key_arg)

# Іноді виникає необхідність, щоб деякі ключові параметри були доступні лише за ключем, 
# а не як позиційні аргументи. 
# Для цього їх треба оголосити після параметра з зірочкою.
def cost_delivery(quantity, *arg, discount = 0):
    suma = 0
    if discount < 0 or discount> 1:
     return "Invalid discount"
    
    if quantity == 1:
        suma = 5
    elif quantity > 1:
        suma = 5 + 2 * (quantity - 1)

    discounted_amount = suma * discount
    suma -= discounted_amount
    return suma