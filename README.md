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