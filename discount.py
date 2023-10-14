def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        if discount > 1:
            print(f"Discount {discount} is more than 1, try again")
            return
        discounted_amount = price * discount
        price -= discounted_amount

    apply_discount()
    return price

price = float(input("Enter price:"))
discount = float(input("Enter discount from 0 to 1: "))

final_price = discount_price(price, discount)
print(f"Ціна вашої ручки: {final_price} грн")