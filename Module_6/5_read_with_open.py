def get_cats_info(path):
    cats_list = []
    with open(path, 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        id, name, age = line.strip().split(',')
        cat_info = {'id': id, 'name': name, 'age': age}
        cats_list.append(cat_info)

    return cats_list
    
        
            
            
    
