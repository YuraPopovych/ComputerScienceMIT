Computer science MIT MOOC

# Week 1
1. problem1. Assume s is a string of lower case characters.

    Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:
    ```
    Number of vowels: 5
    ```
1. problem2. Assume s is a string of lower case characters.

    Write a program that prints the number of times the string 'bob' occurs in s. 
    For example, if s = 'azcbobobegghakl', then your program should print
    ```
    Number of times bob occurs is: 2
    ```
1. problem3(Add refactoring to imporove readability). Assume s is a string of lower case characters.Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print Longest substring in alphabetical order is: beggh. In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
    ```
    Longest substring in alphabetical order is: abc
    ```
# Week 2

   1. bisectionGuessNumber. The program works as follows:
   
        ```
        you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
        The computer makes guesses, and you give it input - is its guess too high or too low?
        Using bisection search, the computer will guess the user's secret number!
        Here is a transcript of an example session:
        Please think of a number between 0 and 100!
        Is your secret number 50?
        Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
        Is your secret number 75?
        Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
        Is your secret number 87?
        Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
        Is your secret number 81?
        Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
        Is your secret number 84?
        Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
        Is your secret number 82?
        Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
        Is your secret number 83?
        Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
        Game over. Your secret number was: 83
        ```

   3. gcdIter.Find the greatest common division of two positive integer iteratively.
   
   4. gcdRecur.Find the greatest common division of two positive integer recursively.
   
   5. polysum. Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
   6. hangManFunctions.helperFunctions.isWordGuessed. Implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.
   
   Example Usage:
    
        ```
        >>> secretWord = 'apple' 
        >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        >>> print(isWordGuessed(secretWord, lettersGuessed))
        False
        ```
        
   7. hangManFunctions.helperFunctions.getGuessedWord. Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord.
   Example Usage:
        ```
        >>> secretWord = 'apple' 
        >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        >>> print(getGuessedWord(secretWord, lettersGuessed))
        '_ pp_ e'
        ```

   8. Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuess.
      Example Usage:
    
        ```
        >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        >>> print(getAvailableLetters(lettersGuessed))
        abcdfghjlmnoqtuvwxyz
# Week 3

   hangManGame.
   Here are the requirements for game:
    The computer  select a word at random from the list of available words that was provided in words.txt.
The game interactive; the flow of the game should go as follows:

   At the start of the game, let the user know how many letters the computer's word contains.

   Ask the user to supply one guess (i.e. letter) per round.

   The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.

   After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.
    Some additional rules of the game:

   A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).

   A user loses a guess only when s/he guesses incorrectly.

   If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try again.

   The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.

# Week 4
WordGame.

In this problem set, you'll implement two versions of a wordgame!

Let's begin by describing the 6.00 wordgame: This game is a lot like Scrabble or Words With Friends, if you've played those. Letters are dealt to players, who then construct one or more words out of their letters. Each valid word receives a score, based on the length of the word and the letters in that word.

The rules of the game are as follows:

Dealing

   A player is dealt a hand of n letters chosen at random (assume n=7 for now).

   The player arranges the hand into as many words as they want out of the letters, using each letter at most once.

   Some letters may remain unused (these won't be scored).

Scoring

   The score for the hand is the sum of the scores for each word formed.

   The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.

  Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

  For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

  As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).

