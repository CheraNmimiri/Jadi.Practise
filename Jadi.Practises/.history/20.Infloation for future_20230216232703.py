typ=int(input("Enter this year price for commodity:"))
fy=int(input("Enter following year for check price:"))
inflation=float(input("Enter inflation now percent:"))
inf=(inflation/100)+1
for i in range(1,fy+1):
    price=typ*inf
    print(f"in {i} year, price equal {price}")
    price=price*inf