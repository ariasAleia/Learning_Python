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
