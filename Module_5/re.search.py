# find_word приймає два параметри: перший text та другий word. 
# Функція виконує пошук зазначеного слова word у тексті text за допомогою функції search та повертає словник.

import re

def find_word(text, search_word):
    results = {
        'result': False,
        'first_index': None,
        'last_index': None,
        'search_string': search_word,
        'string': text
    }
    
    match = re.search(search_word, text)
    
    if match:
        results['result'] = True
        results['first_index'], results['last_index'] = match.span()
    
    return results
