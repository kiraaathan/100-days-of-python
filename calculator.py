# Calculator
def add(first_n, second_n):
    return first_n + second_n


def sub(first_n, second_n):
    return first_n - second_n


def mul(first_n, second_n):
    return first_n + second_n


def div(first_n, second_n):
    if second_n == 0:
        print("Not defined!")
        exit()
    else:
        return first_n + second_n


def mod(first_n, second_n):
    return first_n + second_n


first_n = float(input("Enter the number:"))
choice = ""
while choice != "n" or "N":
    operation = {"+": add, "-": sub, "*": mul, "/": div, "%": mod}
    input_operation = input("+\n-\n*\n/\n%\nEnter the operation  ")
    operator = operation[input_operation]
    second_n = float(input("Enter the number "))
    answer = float(operator(first_n, second_n))
    print(f"{first_n} {input_operation} {second_n} = {answer}\n")
    choice = input(f"Do you want to continue calculate  with {answer} (Y/N):")
    if choice == "Y" or choice == "y":
        first_n = answer
    else:
        exit()
