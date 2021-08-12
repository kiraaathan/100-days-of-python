# find day of the week from the given date

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]

date = input("Enter the date in the format DD/MM/YYYY: \n")
(day, month, year) = [int(i) for i in date.split("/")]

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(f"leap year: {year}")
    days_in_month[1] = 29

day_of_the_week = 0

for i in range(month - 1):
    day_of_the_week += days_in_month[i]

day_of_the_week += day + year + (year // 4) - 2
day_of_the_week = day_of_the_week % 7
print(f"{date} - {days_of_week[day_of_the_week]}")
