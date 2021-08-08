# fizzbuzz

try:
    limit = int(input("Enter a limit: "))
    if limit < 0:
        raise ValueError
except ValueError:
    print("Enter a valid limit!")
    exit()

for i in range(1, limit + 1):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
