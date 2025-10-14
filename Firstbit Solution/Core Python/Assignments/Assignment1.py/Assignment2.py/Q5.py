# WAP to calculate selling price of book based on cost price and discount.

CP = int(input("Enter the Cost Price: "))
D = int(input("Enter the Discount: "))

# Discount Amount 
Discount_Amount = (CP * D) / 100

# Selling Price
Selling_Price = CP - Discount_Amount

print(f'Sellinf Price is {Selling_Price}')

