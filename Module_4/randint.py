# get_random_password буде генерувати випадковий рядок пароля.

from random import randint

def get_random_password():
    passw = ""
    while len(passw) < 8:
        random_num = randint(40, 126)
        num = chr(random_num)
        passw += num
    return passw
    
    
    
        
        
        
    