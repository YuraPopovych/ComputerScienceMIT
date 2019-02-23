def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    tempSecretWord = []
    guessedLetters  = ''
    
    for secretLetter in secretWord:
        tempSecretWord.append(secretLetter)

    lettersGuessedLen = len(lettersGuessed)
    secretWordLen = len(secretWord)
    guessedWordsAndPosition = {}
    for letterGuessedIndex in range(lettersGuessedLen):
        letterGuessed = lettersGuessed[letterGuessedIndex]
        for secretLetterIndex in range(secretWordLen):
            secretLetter = secretWord[secretLetterIndex]
            if letterGuessed == secretLetter:
                tempSecretWord.remove(secretLetter)
                guessedWordsAndPosition[secretLetterIndex] = secretLetter
            if len(tempSecretWord) == 0 :
                return secretWord

    for wordIndex in range(secretWordLen):
        if wordIndex in guessedWordsAndPosition:
            guessedLetters += guessedWordsAndPosition[wordIndex]
        else:
            guessedLetters += '_ '
        
    return guessedLetters

# secretWord = 'apple' 
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))

