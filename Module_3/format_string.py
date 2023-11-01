# Якщо довжина вихідного рядка більша або дорівнює length, ми повертаємо його в тому ж вигляді;
# Якщо вона менша length, ми додаємо попереду рядка пробіли в кількості (length - len(string)) // 2.

def format_string(string, length):
    if len(string) >= length:
        return string
    
    total_spaces = (length - len(string)) // 2
    spaces = " " * total_spaces
    return spaces + string 
