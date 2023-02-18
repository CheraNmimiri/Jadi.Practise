from math import pow,floor
liter=int(input("Enter amount of water:"))
weight_one_liter=0.950
weight_liter=liter*weight_one_liter
molecule=3*pow(10,-23)
aom=(weight_liter)/molecule
aom=floor(aom)
print(f"amount of molecule of {liter} = {aom} ")