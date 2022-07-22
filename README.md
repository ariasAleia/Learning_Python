# Learning Python

I will begin soon a new phase and it is really important to get ready. In this repo I will trace the progress in this path of learning python. Jap, I have already programmed in Python but I want to relearn and learn again. 



<p style="text-align:right;"><b> "A journey of a thousand miles begins with a single step </b>"</p>


## Taking the first steps 

How will I do it? Well... I will follow this [tutorial](https://www.youtube.com/watch?v=rfscVS0vtbw) and take note of the important things that I find in the way. 

Stay tunned! This is just the beginning!

## Syntax, variables, basic functions and structures




### Types of data

__Variable:__ Basically a container to store data values

* **Strings:** Basically plain text
* **Numbers:** Integers or decimal numbers
* **Booleans:** True or False

**Name of variables:** Separate them with underscore. Example: 
```python
character_name = "John"
```
### Strings!

There is sth really cool in Python. We can use many functions concatenated. Kinda decorator pattern

```python
phrase = "Learning Python"
print(phrase.upper().isupper())
```

First function: Makes everything uppercase. Second function: tells us if everything is uppercase or not. Returns a boolean, true or false. Yep. That's exactly the decorator pattern.

We can compare strings directly with ==

```python
print("If we want to print sth but it's extremely large we can "
      "simply split it like this")
```

### Parameters and arguments

When we declare a function we have parameters. For example:
```python
def createNewString(a, b):
    ...
```
a and b are called parameters

When we call the function we have arguments.

```python
createNewString(a_sample, b_sample)
```
a_sample and b_sample are called arguments

### Input

But before that... There is sth interesting. With the extension code runner we can press ctrl + alt + n and we get the output directly. However, if we ask for an user input this won't work since we cannot modify the output. For those cases, we gotta run the code directly in the terminal. But the good news are... chan chaaan chaaannnn. We can set sth in the extension to do exactly that! See [this video](https://www.youtube.com/watch?v=Si8rN5J249M) for more info.


By default the input will be taken as string.
```python
name = input("Enter your name: ")
```

If we want it to be integer for example, we must specify it.

```python
age = int(input("Enter your age: "))
```
```python
a = float(input("Enter the first integer: "))
b = float(input("Enter the second integer: "))
```
### Lists

We can put whatever we want in a list :D 

Long life to the lists!

```python
friends = ["Feliponcio", "Dan", "Cristian"]
print(friends)
```

And when we use negatives it begins to index from the back of the list. -1 would give the very last one, -2 one before the last one and so on...

We can choose also portions of the list
```python
print(friends[1:])
```

#### Add lists together

```python
friends = ["Feliponcio", "Dan", "Cristian", "Sebas"]
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends.extend(lucky_numbers)
print(friends)

```

#### Append elements to a list
```python
lucky_numbers = [4, 8, 15, 16, 23, 42]
lucky_numbers.append(9)
print(lucky_numbers)

```

#### Insert an item in a certain position
```python
lucky_numbers.insert(2, 17)
print(lucky_numbers)
```

#### Remove an item
```python
lucky_numbers.remove(15)
print(lucky_numbers)
```

#### Remove an item by index but printing it before
```python
lucky_numbers.pop()
print(lucky_numbers)
```

Without index it deletes the last item. With index it deletes the item with that index
```python
lucky_numbers.pop(2)
print(lucky_numbers)
```

#### To find the index of an item in the list
```python
print(friends.index("Cristian"))
```

#### To find how many times we have an item in a list
```python
friends[4] = "New friend"
friends[6] = "New friend"
print(friends.count("New friend"))
```

#### Clear list
```python
friends.clear()
```

#### Sort list in ascending order
```python
print(friends)
friends.sort()
print(friends)
```

#### Reverse the order of a list
```python
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
```

#### HEY! Important to copy a list
Jap... We cannot copy that easy. It would modify both lists. 

They both point to the same list. Don't believe me? Then take a peek.
```python
other_friends = friends
print(other_friends)
other_friends.append("Sam")
print(other_friends)
print(friends)
```

If we want to copy we gotta use the function copy to create another list that has the same content but that is independent.

```python
other_friends = friends.copy()
print(other_friends)
other_friends.append("Sam2")
print(other_friends)
print(friends)
```

### Tuples...

Ok. Let's imagine that we have some sort of data that won't be ever changes. It was created and will keep in that way until the rest of our days. Immortal. Immutable. Well... In that case, it would be useful to use tuples. 

Basically, tuples are used when we want to store immutable data. The syntax difference is that in this case we use parentheses () instead of brackets. 

And that's it!

Ok! Wait! Important **We cannot modify the values in a tuple. We can only access to it**. And how do we access to it? Wellm it's the same thing as with a list

```python
coordinates = (4, 5)
print(coordinates)
print(coordinates[1])
```
If we try to modify a value of the tuple it will give us an error

```python
coordinates[0] = 2
```

#### List of tuples

YEAH! Let's break the world!

```python
#Something cool: A list of tuples

#We can do this...
list = [(8,9), (7,8), (6,7)]
print(list)
list[0] = 4
print(list)

#But not this:
list[1][1] = 4
print(list)
```

#### Tuple of lists
```python
#And if we do a tuple of lists?
tuple_of_lists = ([4,5], [5,6])
print(tuple_of_lists)

#We can modify the list in the tuple
tuple_of_lists[0][1] = 3
print(tuple_of_lists)

#But we cannot modify the tuple itself
tuple_of_lists[0] = [4,3]
print(tuple_of_lists)
```

### Functions

The name of a function must be lowercase and separated by underscore to improve readability

```python
def say_hi():
    print("Hello User")

def say_hi_user(name, age):
    print("Hello " + name + " You are " + str(age))
    
say_hi()
say_hi_user("Aleia", 22)
```

After a return statement inside of a function nothing will be executed!

### IF
 
Well... it is way easier with an example
```python
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not male and you are tall")
else:
    print("You are neither male nor tall")
```


### Dictionaries

Store information with key values. Sorry... what?
Well, let's see. How does a dictionary work? Well, we have a word and we have a definiction, don't we? Well, that's exactly how a dictionary works. With this data structure, the key would be like the word and the value would be like the definition.

The difference here is that we do it inside curly brackets: {}

And other important thing: All of the keys must be unique. If not, it could work but return just one of the values that have the key.

```python
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December" 
}
```

And we can look for the value having the key. For example:

```python
print(month_conversions["Dec"])
#Or also:
print(month_conversions.get("Jan"))
```

It seems that [] and .get() make exactly the same thing but the good thing about .get() is that we can specify a default value to be returned in case that we enter a key that is not found in the dictionary.

```python
print(month_conversions.get("Dec"))
print(month_conversions.get("Derc"))
print(month_conversions.get("Derc", "Key was not found :P"))
```

### While loops
```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

### For loops

With a for we basically iterate through a collection. A collection can be a string, a list, a tuple, a dictionary...
For example with a string! That's cool.

```python
for letter in "Aleia is coding":
    print(letter)
```
Or with a list:
```python
friends = ["You", "Me", "We both"]
for friend in friends:
    print(friend)
```

And in a not so pythonic way we can also iterate through a list:
```python
for index in range(len(friends)):
    print(friends[index])
```

And of course in a range of given numbers:
```python
for i in range(10):
    print(i)
#Output: 0 1 2 3 4 5 6 7 8 9
for i in range(3, 10):
    print(i)
#Output: 3 4 5 6 7 8 9
```

**REALLY IMPORTANT:** In range we don't take the last limit. It's an open interval at the end. Example: range(10), from 0 to 9! Other example: range(4,8) that would be from 4 to 7!!!

### Two dimensional lists

Yep. Like matrix!

```python
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])
```

### Nested loops:

```python
for list in number_grid:
    for item in list:
        print(item)
```

### Translator
Interesting thing. We can check in Python if sth is inside of other thing doing this:

```python
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation
```

And remember! We can concatenate strings! That's sth really useful.

That could be done better if we for example do this:
```python
... 
if letter.lower() in "aeiou":
    ...
```

### Comments

```python
# This is a comment
'''
and this is also another comment. Cool
'''
# This is a comment
```
But officially is better to use the #

### Try and except

This one is important Aleia. Pay attention!

```python
try:
    number = int(input("Enter a number: "))
    value = 10 / number
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError as err:
    print(err)
```

As we could see, we can print sth that we want or we want directly print the message that comes with the expection that we caught

### Reading files with Python :D

If both files are in the same folder, then we just need the name of the file... However in our case we had to specify first the folder where it was. Kinda strange but it worked...

The second parameter specifies if we want to read or modify or write the file
r means that we only want to read from it

w is that we want to write in the file, change it
a means append, we can add new info to the file
r+ -> means read and write

**Warning:** Read from the file only once. If not we will have problems with the cursor!

```python
employee_file = open("employees.txt", "r")
#This returns a True if we can read it. (if we have "r": True, if we have "w", for example: False)
print(employee_file.readable())

#To read lines in the file but it moves the cursor so that the next time when we want to read it won't
#read the whole file. Better not use it

# print(employee_file.readline())
# print(employee_file.readline())

#To get all the info from the file but it moves the cursor so that the next time when we want to read it won't
#read the whole file. Better not use it:

# print(employee_file.read())

#Sth that we can do that is actually faaar better is:
list_of_employees = employee_file.readlines()

#But  again!!! it moves the cursor so that the next time when we want to read it won't
#read the whole file. Better not use it more than once. It's better to save it in a variable

#With that we have all the info saved in a list

#And now we can do magic!

for employee in list_of_employees:
    print(employee)
    
#Or just take one specific value:
print("Just one employee: " + list_of_employees[2])


#Remember to close the file!
employee_file.close()

```

### Append in files

No more "r" now we go with "a".
Here we will basically open a file and append info to it, that means that we will add info at the end of the file.

More info just check the script *appender.py* but hey! be careful!!! If you run the code multiple times, it will add the new line many times and it can get messy

### Write in files (modify them)

Jap. We can also do it. Instead of "a", we have now "w" as a second parameter.

### Modules

A module is any external file (.py) that we have in python.
We can import files into the file we are working on. For example, useful_tools was a file that we created with the name useful_tools.py

```python
import useful_tools

# and now we can access to all the things we have in the file called useful_tools

print(useful_tools.get_file_ext("cuento.pdf"))
print(useful_tools.beatles[0])
print(useful_tools.roll_dice(90))
```

And we can find a huuuuuuuuuuuuge amount of modules. Just google list of modules in python. And we can then find how we import them :)

Yep, Python community is great. People doing magic together. Here a sample link: [Python modules.](https://docs.python.org/3/py-modindex.html) 

But the question now is... Where are all those external modules saved? Yeah, we know that there are some built-in modules to which we can have direct access but... What about the other ones? Where are they stored? 