# перший стовпець — ширина 4 символи, вирівнювання по правому краю
# другий стовпець — ширина 10 символів, вирівнювання по лівому краю
# третій та четвертий стовпець — ширина 5 символів, вирівнювання по центру
# вертикальний символ | не входить у ширину стовпця

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    formatted_list = []
    
    for index, (student_name, grade_letter) in enumerate(students.items(), 1):
        grade_number = grades[grade_letter]
        
        formatted_str = "{:>4}|{:<10}|{:^5}|{:^5}".format(index, student_name, grade_letter, grade_number)
        
        formatted_list.append(formatted_str)

    return formatted_list