def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    tempSecretWord = []
    
    for secretLetter in secretWord:
        tempSecretWord.append(secretLetter)
    
    for letterGuessed in lettersGuessed:
        for secretLetter in secretWord:
            if letterGuessed == secretLetter:
                tempSecretWord.remove(secretLetter)
            if len(tempSecretWord) == 0 :
                return True
    return False