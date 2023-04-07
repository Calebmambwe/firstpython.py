secret_word = "gg"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while secret_word != guess and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Please enter secret word ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
        print("You lose")
elif guess == secret_word:
        print("Yea you win")
