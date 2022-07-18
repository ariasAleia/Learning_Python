def calculate(a, b, sign):
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "*":
        return a * b
    elif sign == "/":
        return a / b
    elif sign == "**":
        return a ** b
    else:
        print("Not a valid operation")


print("Welcome to your better version calculator")
num1 = float(input("Enter the first number: "))
sign = input("Enter operation to be made (+, -, *, /, **): ")
num2 = float(input("Enter the second number: "))

print(calculate(num1, num2, sign))
