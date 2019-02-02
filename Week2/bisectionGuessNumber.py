min = 0
max = 100
guess = (min + max ) / 2
answer = None
allowed_symbol_in_answer = "hlc"

print("Please think of a number between 0 and 100!")
while answer != "c":
    print("Is your secret number ", end="")
    print( str(guess) + "?" )
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if answer == "l":
        min = guess
    if answer == "h":
        max = guess
    if answer not in allowed_symbol_in_answer:
        print("Sorry, I did not understand your input.")
        
    guess = int ( (min + max) / 2) 

print("Game over. Your secret number was:", guess)

