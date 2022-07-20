def raise_to_power(base, exponent):
    ans = 1
    for i in range (exponent):
        ans = ans * base
    return ans

print(raise_to_power(2, 3))