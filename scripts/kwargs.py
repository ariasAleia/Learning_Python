def total_fruits(**kwargs):
    ans = 0
    for fruit_value in kwargs.values():
        ans += fruit_value
    return ans

#Take care, when passing the elements don't do it as when you create a normal dictionary, pass it
#directly with commas and with =

#The following wouldn't work for example:
#print(total_fruits({"banana":5, "mango":7, "apple":8}))

print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))