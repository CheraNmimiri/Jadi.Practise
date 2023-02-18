from math import pow
velocity=float(input("'Enter velocity of air:"))
temp=float(input("Enter temperature of air:"))
wci=(13.12+(0.6215*temp))- (11.37*pow(velocity,0.16))+ (0.3965*temp*pow(velocity,0.16))
print("The wind chill index is : %.0f" % (wci))
print("The temperature is :", int(round(wci,0)))
