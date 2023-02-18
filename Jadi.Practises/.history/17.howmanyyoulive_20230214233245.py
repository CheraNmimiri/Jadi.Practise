import jdatetime
birthday_year=int(input("Enter your birthday year:"))
birthday_month=int(input("Enter your birthday month:"))
birthday_day=int(input("Enter your birthday day:"))
print(jdatetime.datetime.today())
hmy=1401-birthday_year
hmmo=(hmy*12)-birthday_month
if birthday_month
    hmd=(hmmo*365)
hmh=hmd*24
hmm=hmh*60
hms=hmm*60
print("you age is %d ,you are live for %d month and %d and days and %d hours and %d minutes and %d seconds. " % (hmy,hmmo,hmd,hmh,hmm,hms))


