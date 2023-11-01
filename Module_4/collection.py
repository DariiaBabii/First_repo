# calculate_distance, яка на вхід приймає список координат чотирикутника зі словника виду [0, 1, 3, 2, 0]. 
# Функція повинна підрахувати, використовуючи вказаний словник, 
# яку загальну відстань пролетить дрон, рухаючись між точками польоту.

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if len(coordinates) <= 1:
        return 0
    path = 0
    for i in range(len(coordinates) - 1):
        key = tuple(sorted((coordinates[i], coordinates[i+1])))
        
        if key in points:
            path += points[key]
    return path 