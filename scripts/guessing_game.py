# My first attempt:

# secret_word = "sth"
# word_was_found = False

# while not (word_was_found):
#     user_word = input("Try to guess. Enter the word: ")
#     if user_word.lower() == secret_word.lower():
#         print("You guessed the word!")
#         word_was_found = True
#     else:
#         print("That's not the word. Keep trying")

# print("End of the game")

#A shorter (and maybe better) way to do it:

secret_word = "apple"
user_word = ""
attempt = 1
guess_limit = 3

while user_word != secret_word and attempt <= guess_limit:
    user_word = input("(Attempt " + str(attempt) + ")Enter your guess: ")
    attempt += 1

if user_word == secret_word:
    print("You win :D")
else:
    print("Sorry, you lost. The word is " + secret_word)