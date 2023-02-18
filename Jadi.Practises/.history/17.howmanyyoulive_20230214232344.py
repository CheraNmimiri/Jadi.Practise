birthday_year=int(input("Enter your birthday year:"))
birthday_month=int(input("Enter your birthday month"))

this_year=1401
hmy=1401-birthday_year
hmmo=hmy*12
hmd=hmmo*365
hmh=hmd*24
hmm=hmh*60
hms=hmm*60
print("Now %d and you age is %d ,you are live for %d month and %d and days and %d hours and %d minutes and %d seconds. " % (this_year,hmy,hmmo,hmd,hmh,hmm,hms))


