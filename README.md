# Introduction-to-Computer-Science-and-Programming-Using-Python
MITx: 6.00.1x

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