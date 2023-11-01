def sanitize_phone_number(phone):
    phone_num = phone.strip()
    chars_to_remove = "(-)+ "  # символи для видалення
    cleaned_input = phone_num.translate(str.maketrans('', '', chars_to_remove))
    
    return cleaned_input
    
        
        
        
        
        
        
    
    