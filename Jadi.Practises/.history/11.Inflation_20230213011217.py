first_price=float(input("Enter first year price:"))
second_price=float(input("Enter second year price:"))
inflation=(second_price-first_price)/(first_price*100)
third_price=second_price+(second_price*inflation)
print("Price in third year is %d and inflation is %d%% ." )

