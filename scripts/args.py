def sum(num1, num2):
    return num1 + num2

#And what if the function receives now 4 numbers?

def sum2(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4


print(sum(2, 3))
print(sum2(2, 4, 5, 7))
#And what if we have now 100 numbers... Are you kidding me?
#I have better things to do (Do I? :P)

#There must be a better way to handle this: Yep. *args and *kwargs

def sum(*args):
    ans = 0
    for num in args:
        ans += num
    return ans
print(sum(2, 3))
print(sum(2, 4, 5, 7))

#It's beautiful!!!
