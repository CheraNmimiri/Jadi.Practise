first_price=float(input("Enter first year price:"))
second_price=float(input("Enter second year price:"))
inflation=float((second_price-first_price)/(first_price))
amount=(second_price+second_price)*inflation
print("Prediction price of third year is %d and amount of inflation is %f%%." % (third_price,inflation))

