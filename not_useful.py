# def prepare_data(data):
#         if len(data) <= 1:
#                 return data
#         else:
#             data.sort()
#             data.pop(0)
#             data.pop(-1)
#             return data



          

# def format_ingredients(items):
#      if not items:
#         return ""
#      elif len(items) == 1:
#         return items[0]
#     # Якщо в списку два елементи
#      elif len(items) == 2:
#         return " and ".join(items)
#     # Для списків із більше ніж двома елементами
#      else:
#         return ", ".join(items[:-1]) + " and " + items[-1]

# Тестування
# print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))




# def get_grade(grade):
#     key = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
#     return key.get(grade)

# def get_description(grade_des):
#     key = {
#         "F": "Unsatisfactorily",
#         "FX": "Unsatisfactorily",
#         "E": "Enough",
#         "D": "Satisfactorily",
#         "C": "Good",
#         "B": "Very good",
#         "A": "Perfectly"
#     }
#     return key.get(grade_des)


# def lookup_key(data, value_to_find):
#     matching_keys = []
#     for l, current_value in data.items():
#         if value_to_find == current_value:
#             matching_keys.append(l)
#     return matching_keys
      
from pathlib import Path

# def parse_folder(path):
#     files = []
#     folders = []
#     for item in path.iterdir():
#         if item.is_file():
#             files.append(item)
#         else:
#             folders.append(item)         
        
            
#     return files, folders
        
        
# def find_articles(key, letter_case=False):
#     result = []
    
#     for item in articles_dict:
        
#         for field in ["title", "author"]:
#              if letter_case:
#                  if key in item[field]:
#                     result.append(item)
#                     break
#              else:
#                  if key.lower() in item[field].lower():
#                     result.append(item)
#                     break

#     return result   

# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone


# def get_phone_numbers_for_countries(list_phones):
#     phone_dict = {
#     'UA': [],
#     'JP': [],
#     'TW': [],
#     'SG': []
# }

#     Japan = list_phones.find(81)
#     Singapore = list_phones.find(65)
#     Taiwan = list_phones.find(886)
#     Ukraine = list_phones.find(380)

#     if Japan != -1:
#         phone_dict['JP'].extend(Japan)
#     if Singapore != -1:
#         phone_dict['SG'].extend(Singapore)
#     if Taiwan != -1:
#         phone_dict['TW'].extend(Taiwan)
#     if Ukraine != -1:
#         phone_dict['UA'].extend(Ukraine)
#     return phone_dict

        
        
            
# Japan	JP	+81
# Singapore	SG	+65
# Taiwan	TW	+886
# Ukraine	UA	+380   
            
        
# import re

# def replace_spam_words(text, spam_words):
#     # Функція для заміни спам-слова зірочками
#     def asterisk_replacer(match):
#         return '*' * len(match.group(0))  # створюємо рядок з зірочок довжиною у спам-слово

#     for word in spam_words:
#         # Замінюємо кожне спам-слово на зірочки з урахуванням регістру
#         # re.IGNORECASE допомагає робити пошук без урахування регістру
#         pattern = re.compile(re.escape(word), re.IGNORECASE)
#         text = pattern.sub(asterisk_replacer, text)

#     return text

# # Тестовий виклик:
# text = "This is a bad and terrible sentence."
# spam_words = ["bad", "terrible"]
# print(replace_spam_words(text, spam_words))

    
def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for sublist in employee_list:
        for item in sublist:
            fh.write(item + "\n")
        if sublist != employee_list[-1]:  # якщо це не останній підсписок, додаємо додатковий рядок
            fh.write("\n")
    fh.close()
    
    
    
        
        
        
              
        
            
        
            
    
    
        
        
        
        
        
        
    
    
    