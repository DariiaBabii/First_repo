def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for sublist in employee_list:
        for item in sublist:
            fh.write(item + "\n")
        if sublist != employee_list[-1]:  # якщо це не останній підсписок, додаємо додатковий рядок
            fh.write("\n")
    fh.close()
        
            
                