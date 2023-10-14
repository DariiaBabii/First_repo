def discount_price(price, discount):
    if discount > 1:
        return "Invalid discount"
    return price - price * discount

price_input = input("Enter price: ").replace(',', '.')
discount_input = input("Enter discount from 0 to 1: ").replace(',', '.')

if price_input.isnumeric() and discount_input.isnumeric():
    price = float(price_input)
    discount = float(discount_input)
    print(discount_price(price, discount))
else:
    print("Invalid input")
