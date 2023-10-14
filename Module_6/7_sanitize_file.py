import re

def sanitize_file(source, output):
    with open(source, 'r') as fh:
        content = fh.read()
        
    cleaned_content = re.sub(r'\d', '', content)
    
    with open(output, 'w') as file:
        file.write(cleaned_content)

        
