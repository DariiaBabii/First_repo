# Функція обчислюватиме середнє арифметичне типу Decimal з кількістю значущих цифр signs_count. 
# Параметр number_list — список чисел

from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count

    
    sum_num = Decimal(0)
    for i in number_list:
        sum_num += Decimal(i)
        average = sum_num / Decimal(len(number_list))
    return average
    
    
        
    