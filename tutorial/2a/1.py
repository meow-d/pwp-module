selling_price = int(input("Enter the selling price: "))
buying_price = int(input("Enter the buying price: "))

if selling_price > buying_price:
    print("You have a profit in trading this item.")
else:
    print("You have a loss in trading this item.")
