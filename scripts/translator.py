#This translator has an unique way to express things in the Giraffe language

#Giraffe language
#vowels -> g

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation
        

print("Welcome to the translator to Giraffe language!")

user_phrase = input("Enter a phrase: ")
print("Translated into Giraffe Language it would be:\n"
      + translate(user_phrase))
        