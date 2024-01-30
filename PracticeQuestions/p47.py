# calculate discount
def calculate_discount(price,dis):
    return price - ((dis / 100) * price)

price = float(input("enter price: "))
dis = float(input("enter discount: "))
print(f"final price = {calculate_discount(price,dis)}")