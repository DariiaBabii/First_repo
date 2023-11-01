# parse_folder приймає єдиний параметр path, який є об'єктом Path. 
# Функція повинна просканувати директорію path та повернути кортеж із двох списків. 
# Перший — це список файлів усередині директорії, другий — список директорій.

from pathlib import Path

def parse_folder(path):
    files = []
    folders = []
    for item in path.iterdir():
        if item.is_file():
            files.append(item.name)
        else:
            folders.append(item.name)         
                    
    return files, folders