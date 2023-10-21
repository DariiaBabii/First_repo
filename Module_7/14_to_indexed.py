# Напишіть функцію to_indexed(source_file, output_file), 
# яка зчитуватиме вміст файлу, додаватиме до прочитаних рядків порядковий номер 
# і зберігати їх у такому вигляді у новому файлі.

# Кожний рядок у створеному файлі повинен починатися з його номера, 
# двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.

# Нумерація рядків іде від 0.

def to_indexed(source_file, output_file):
    with open(source_file, 'r') as source_fh:
        lines = source_fh.readlines()

    with open(output_file, 'w') as output_fh:
        for line_number, line in enumerate(lines, start=1):
            indexed_line = f"{line_number}: {line}"
            output_fh.write(indexed_line)

# Приклад використання:
source_file = 'source.txt'
output_file = 'indexed_output.txt'
to_indexed(source_file, output_file)

    
    
        
    
        
            