def read_employees_from_file(path):
    fh = open(path, 'r')
    lines = fh.readlines()
        
    # видалення пробілів та символів нового рядка з кожного рядка
    cleaned_lines = [line.strip() for line in lines]
  
    fh.close()
    return cleaned_lines
 
    
    
        
    
