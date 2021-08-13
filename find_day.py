# Find day of the week from the date

print("Enter the date in (DD/MM/YY) format")
print("Day:")
day = int(input())
print("Month:")
month = int(input())
print("Year:")
year = int(input())

# first two digit of year

first_2yr = int(str(year)[:2])

# last two digits

last_2digit = year % 100

# centuary code

c_code = int(first_2yr % 4)

if c_code == 0:
    cc = 6
elif c_code == 1:
    cc = 4
elif c_code == 2:
    cc = 2
else:
    cc = 0

# year code

yc = int((last_2digit + (last_2digit / 4)) % 7)

if month == 1:
    if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
        mc = -1
    else:
        mc = 0
elif month == 2:
    if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
        mc = 2
    else:
        mc = 3
elif month == 3:
    mc = 3
elif month == 4:
    mc = 6
elif month == 5:
    mc = 1
elif month == 6:
    mc = 4
elif month == 7:
    mc = 6
elif month == 8:
    mc = 2
elif month == 9:
    mc = 5
elif month == 10:
    mc = 0
elif month == 11:
    mc = 3
else:
    mc = 5

# calculation formula

h = int((cc + yc + mc + day) % 7)

if h == 0:
    print("Sunday")
elif h == 1:
    print("Monday")
elif h == 2:
    print("Tuesday")
elif h == 3:
    print("Wednesday")
elif h == 4:
    print("Thursday")
elif h == 5:
    print("Friday")
elif h == 6:
    print("Saturday")
else:
    print("Invalid entry!")
