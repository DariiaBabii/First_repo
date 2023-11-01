
# Для класу Animal у конструкторі створіть дві властивості: nickname - кличка тварини 
# та weight - вага тварини. Реалізуйте також метод класу say. 
# реалізуйте в класі Animal метод change_weight, який має змінювати вагу тварини.
# Викличте функцію change_weight(12) для об'єкта animal 
# та змініть значення початкової ваги з 10 на 12 одиниць.

# Додамо в клас Animal змінну класу color, значення якої спочатку дорівнює 'white', 
# і метод change_color, який повинен змінювати значення змінної класу color.

# Створіть екземпляри об'єкта: first_animal та second_animal

# Викличте функцію change_color("red") для будь-якого екземпляра об'єкту Animal 
# та змініть значення змінної класу color на "red".

class Animal:
    color = "white"
    

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
  

    
    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

    def change_color(self, new_color):
        self.color = new_color
        
    
    


animal = Animal("Simon", 10)
animal.change_weight(12)

first_animal = Animal("Simon", 10)

second_animal = Animal("John", 12)

Animal.color = "red"


