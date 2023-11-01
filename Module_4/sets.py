# is_valid_pin_codes буде приймати як параметр список цих пін-кодів — рядок з чотирьох цифр 
# і повертати логічне значення — валідний список чи ні. 
# Переконайтеся, що серед цих пін-кодів у списку не буде дублікатів, 
# всі вони зберігаються у вигляді рядків, їх довжина дорівнює 4 символам і містять вони тільки цифри.

def is_valid_pin_codes(pin_codes):
    if not pin_codes:
        return False

    if len(pin_codes) != len(set(pin_codes)):
        return False

    for i in pin_codes:
        if len(i) != 4:
            return False

        if not i.isdigit():
            return False
    return True
    
    
        
    
        
    
        
            
        
            
        
            
    