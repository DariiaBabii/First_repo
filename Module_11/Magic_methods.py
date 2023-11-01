# Створіть клас Point, який відповідатиме за відображення геометричної точки на площині.
# Реалізуйте через конструктор __init__ ініціалізацію двох атрибутів: координати x та координати y.

# Приклад:

# point = Point(5, 10)

# print(point.x)  # 5
# print(point.y)  # 10

# У класу Point через конструктор __init__ оголошено два атрибути: координати x та y. 
# Приховати доступ до них з допомогою подвійного підкреслення: __x та __y

# Реалізуйте для класу Point механізми setter та getter до атрибутів __x та __y 
# за допомогою декораторів property та setter.

# У класу Point до механізму setter властивостей x і y додайте перевірку на значення, що вводиться. 
# Дозвольте встановлювати значення властивостей x та y для екземпляра класу, 
# тільки якщо вони мають числове значення (int або float).

from random import randrange

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y
        
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, x):
        if (type(x) is int) or (type(x) is float):
            self.__x = x


    @y.setter
    def y(self, y):
        if (type(y) is int) or (type(y) is float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"



# Реалізуйте клас Vector. Властивість coordinates визначає координати вектора і є екземпляром класу Point. 
# Нагадаємо, що вектором називають спрямований відрізок з початком та кінцем. 
# Початок у нас буде в точці (0, 0), а кінець вектора ми задаватимемо атрибутом coordinates.

# Реалізуйте можливість звертатися до координат екземпляра класу Vector через квадратні дужки:

# vector = Vector(Point(1, 10))

# print(vector.coordinates.x)  # 1
# print(vector.coordinates.y)  # 10

# vector[0] = 10  # Встановлюємо координату x вектора 10

# print(vector[0])  # 10
# print(vector[1])  # 10

# Щоб отримати значення, використовуючи квадратні дужки об'єкта print(vector[0]), 
# реалізуйте метод __getitem__ у класу Vector.

# Для запису значення координат вектора через індекс, як vector[0] = 10, 
# реалізуйте метод __setitem__ у класу Vector.

# Звернення до координати x проводиться за індексом 0, а звернення до координати y - за індексом 1.
        

class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y

# Функтор. Створіть для класу Vector метод __call__. 

# При виклику екземпляра класу як функції він повертає кортеж з координатами вектора.

# Якщо при виклику ми передаємо параметр число, 
# ми виконуємо добуток вектора на число — множимо кожну координату на вказане число та повертаємо кортеж з новими координатами вектора.

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y
    
# операції додавання та віднімання векторів. 
# Тобто перевизначите математичні оператори __add__ та __sub__

# Є два вектори: a з координатами (x1, y1) та b з координатами (x2, y2).
# Тоді додавання векторів b + a - це новий вектор з координатами (x2 + x1, y2 + y1). 
# Віднімання – зворотна операція, b - a - це новий вектор з координатами (x2 - x1, y2 - y1)

    def __add__(self, vector):
        return Vector(Point(self.coordinates.x + vector.coordinates.x, self.coordinates.y + vector.coordinates.y))
          

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))
    
# Реалізуйте для класу Vector операцію скалярного добутку векторів. 
# Тобто перевизначте для нього математичний оператор __mul__

# Є два вектори: a з координатами (x1, y1) та вектор b з координатами (x2, y2).

# Тоді скалярний добуток векторів b*a - це таке число x2*x1+y2*y1.

    def __mul__(self, vector):
        return (self.coordinates.x * vector.coordinates.x + self.coordinates.y * vector.coordinates.y)

# метод визначення довжини вектора - len для класу Vector
# Для вектора a з координатами (x1, y1) його довжина визначається за такою формулою:
# (x1 ** 2 + y1 ** 2) ** 0.5.

    def len(self):
        return ((self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5)

# Реалізуйте для класу Point та Vector магічний метод __str__. 
# Для класу Point метод повинен повертати рядок виду Point(x,y), а для класу Vector - рядок Vector(x,y), 
# як у прикладі нижче (замість x,y необхідно підставити значення координат екземпляра класу):
    
    def __str__(self):
       return f"Vector({self.coordinates.x}, {self.coordinates.y})"

# __eq__(self, other) — визначає поведінку під час перевірки на відповідність (==). реалізація з len()
# __ne__(self, other) — визначає поведінку під час перевірки на невідповідність. !=.
# __lt__(self, other) — визначає поведінку під час перевірки на менше <.
# __gt__(self, other) — визначає поведінку під час перевірки на більше >.
# __le__(self, other) — визначає поведінку під час перевірки на менше-дорівнює <=.
# __ge__(self, other) — визначає поведінку під час перевірки на більше-дорівнює >=.

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len() 
        

    def __lt__(self, vector):
        return self.len() < vector.len() 
        

    def __gt__(self, vector):
        return self.len() > vector.len() 
        

    def __le__(self, vector):
        return self.len() <= vector.len() 
        

    def __ge__(self, vector):
        return self.len() >= vector.len() 
        
# Клас RandomVectors повинен мати метод __iter__, який має повернути об'єкт ітератора (клас Iterable)
# Об'єкт ітератора (примірник класу Iterable) повинен мати метод __next__
# Метод __next__ стежить за кількістю можливих кроків ітерації, вони визначаються параметром max_vectors
# Якщо ми вичерпали можливі кроки, то метод __next__ генерує виняток StopIteration
# В іншому випадку метод __next__ повертає вектор з випадковими координатами (примірник класу Vector), 
# розмір координат вектора визначається параметром max_points.


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = []
        self.points = []
        for i in range(randrange(max_points)):
            self.points.append(Point(randrange(max_points), randrange(max_points)))
        
            

    def __next__(self):
        if self.current_index < len(self.vectors):
            self.current_index += 1
            return self.vectors[self.current_index - 1]
        else:
            raise StopIteration
    
    
class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors = max_vectors
        self.max_points = max_points
        self.vectors = []
        self.points = []
        
        

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)
            

    
    
        
    