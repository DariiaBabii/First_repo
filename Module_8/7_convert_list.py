# Якщо функція convert_list приймає у параметрі cats список іменованих кортежів,
# то функція поверне список словників.
# І в той же час, якщо функція convert_list приймає в параметрі cats список словників, 
# то результатом буде зворотна операція та функція поверне список іменованих кортежів.

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

def convert_list(cats):
    result = []

    # Якщо cats - список іменованих кортежів Cat
    if isinstance(cats, list) and all(isinstance(cat, Cat) for cat in cats):
        for cat in cats:
            result.append({
                'nickname': cat.nickname,
                'age': cat.age,
                'owner': cat.owner
            })
    
    # Якщо cats - список словників
    elif isinstance(cats, list) and all(isinstance(cat, dict) for cat in cats):
        for cat in cats:
            result.append(Cat(**cat))

    return result

