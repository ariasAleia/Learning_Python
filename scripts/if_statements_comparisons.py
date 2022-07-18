def choose_biggest_number(a, b, c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
    
print(choose_biggest_number(7,4,5))