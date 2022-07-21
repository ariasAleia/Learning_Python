try:
    number = int(input("Enter a number: "))
    value = 10 / number
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError as err:
    print(err)