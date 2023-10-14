from collections import deque

MAX_LEN = 10

lifo = deque(maxlen=MAX_LEN)  # використовуйте maxlen для автоматичного обмеження розміру

def push(element):
    lifo.appendleft(element)  # додаємо елемент на початок списку
    return lifo

def pop():
    if lifo:  # перевіряємо, чи є що видаляти
        return lifo.popleft()  # дістаємо та видаляємо елемент з початку списку
    return None  # або повертаємо None, якщо стек порожній
