# Повернемося до завдання розрахунку ціни з урахуванням дисконту та розберемо підхід із позиції карування. 
# Створіть функцію discount_price(discount), 
# яка визначатиме в собі та повертатиме функцію розрахунку реальної ціни з урахуванням знижки.

# Виклик функції discount_price(discount) поверне функцію, яка розраховує ціну на товар зі знижкою, 
# що дорівнює discount .

def discount_price(discount):
    def price(price):
        return price - price * discount
    return price
    
        

    


cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))