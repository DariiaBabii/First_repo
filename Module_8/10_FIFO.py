# Створіть змінну fifo, що містить колекцію deque. 
# Обмежте розмір за допомогою константи MAX_LEN. 
# Функція push додає значення element до кінця списку fifo. 
# Функція pop дістає та повертає перше значення зі списку fifo.

from collections import deque

MAX_LEN = 20

fifo = deque(maxlen=MAX_LEN) 


def push(element):
    fifo.append(element)  
    return fifo


def pop():
    if fifo:  
        return fifo.popleft() 
    return None  