def get_recipe(path, search_id):
    with open(path, 'r') as fh:
        lines = fh.readlines()

    for line in lines:
        split_line = line.strip().split(',', 2)  # Розділіть лише на 3 частини
        if len(split_line) != 3:
            continue  # Пропустіть рядки, які не відповідають очікуваному формату
        id, name, ingredients_string = split_line
        ingredients = ingredients_string.split(',')  # Подальше розділення на інгредієнти

        if id == search_id:
            recipe = {
                'id': id,
                'name': name,
                'ingredients': [ingredient.strip() for ingredient in ingredients]  # видаляємо лишні пробіли
            }
            return recipe

    return None