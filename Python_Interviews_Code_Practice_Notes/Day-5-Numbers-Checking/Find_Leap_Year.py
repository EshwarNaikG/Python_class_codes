# Find Leap year :-

Year = int(input("enter a year : "))

if(Year % 400 == 0) and (Year % 100 == 0):  # Below- 1999
    print(Year, " is a leap year")

elif(Year % 4 == 0) and (Year % 100 != 0):  # Above- 2000
    print(Year, "is a leap year")

else:
    print(f"The given year {Year} is not a leap year")