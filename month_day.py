#Checking no.of days for given month
month = int(input("Enter your month here:"))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Days are 31")
elif month ==2:
    year = int(input("Enter year : "))
    if year%4==0:
        print("Month has 29 Days")
    else:
        print("month has 28 Days")
else:
    print("Month has 30 Days")