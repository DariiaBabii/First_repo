# Створіть клас NumberString, успадкуйте його від класу UserString, 
# визначте для нього метод number_count(self), 
# який буде рахувати кількість цифр у рядку.

from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for value in self:
            if value.isdigit():
                count += 1
        return count
        
        
            
                
                
            
                
        