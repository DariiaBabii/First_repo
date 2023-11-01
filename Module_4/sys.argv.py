# parse_args повертає рядок, складений з аргументів командного рядка, розділених пробілами. 
# Наприклад, якщо скрипт був викликаний командою: python run.py first second, 
# то функція parse_args повинна повернути рядок наступного виду 'first second'.

import sys

def parse_args():
    arguments = sys.argv[1:]
    return ' '.join(arguments)
