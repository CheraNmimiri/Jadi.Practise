typ=int(input("Enter this year price for commodity:"))
fy=int(input("Enter following year for check price:"))
inflation=float(input("Enter inflation now percent:"))
inf=(inflation/100)+1
i=1
while i < fy+1: 
    typ=typ*inf
    print(f"in {i} year, price equal {typ:.}")
    typ=typ*inf
    i+=1