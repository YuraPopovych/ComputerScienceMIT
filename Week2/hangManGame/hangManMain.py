import random
from helperFunctions.getAvailableLetters import getAvailableLetters
from helperFunctions.getGuessedWord import getGuessedWord

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.


      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    letterSGuessed = []
    secretWordListLen = len(secretWord)
    secretWordNumber = random.randrange(0, secretWordListLen)
    secretWord = secretWord[secretWordNumber].lower()
    secretWordLen = len(secretWord)
    guessTry = 8
    print("Loading word list from file...\n{0} words loaded.".format( str(secretWordListLen) ) )
    greeting = "Welcome to the game, Hangman!\nI am thinking of a word that is {0} letters long.".format(secretWordLen)
    print(greeting)
    print("-----------")

    while guessTry > 0:
      print("You have {0} guesses left.".format( str(guessTry)) )
      print("Available letters: {0}".format(getAvailableLetters(letterSGuessed)))
      letterGuessed = input("Please guess a letter:")
      guessedWord = getGuessedWord(secretWord, letterSGuessed)   
      if letterGuessed in letterSGuessed:
        print("Oops! You've already guessed that letter:", guessedWord)
        print("-----------")
      elif letterGuessed in secretWord:
        letterSGuessed.append(letterGuessed)
        guessedWord = getGuessedWord(secretWord, letterSGuessed)
        print("Good guess:", guessedWord)
        print("-----------")
        if guessedWord == secretWord:
          print("Congratulations, you won!")
          return
      else:
        letterSGuessed.append(letterGuessed)
        print("Oops! That letter is not in my word:", guessedWord)
        print("-----------")
        guessTry -= 1
    print("Sorry, you ran out of guesses. The word was {0}.".format(secretWord))
    return
    




loadWords = ['apple', 'Yura', 'Random', 'Ajajajajaja', 'ucu', 'libary', 'apple','bodya','misha', 'javascript', 'clock','kormushka', 'politech']


hangman(loadWords)

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))