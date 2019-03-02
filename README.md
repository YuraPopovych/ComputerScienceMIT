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
