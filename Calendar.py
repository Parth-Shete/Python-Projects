import calendar

print("*********")
print("Calendar")
print("*********")

year = int(input("Enter the year: "))

print("Calendar for year is:- ")  #this is for getting calendar for the whole year
print(calendar.calendar(year))

month = int(input("\nEnter the month: "))  #this is for getting calendar for an individual month
print("Calendar for month is:- ")
print(calendar.month(year, month))
