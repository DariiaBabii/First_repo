# prepare_data видаляє з переданого списку найбільше та найменше значення, 
# сортує його в порядку зростання і повертає змінений список як результат.

def prepare_data(data):
        if len(data) <= 1:
                return data
        else:
            data.sort()
            data.pop(0)
            data.pop(-1)
            return data
    
    
    
    
    