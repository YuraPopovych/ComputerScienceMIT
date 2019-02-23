import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabetical_letters = []
    
    for letter in string.ascii_lowercase:
        alphabetical_letters.append(letter)
    
    for letterGuessed in lettersGuessed:
        if letterGuessed in alphabetical_letters:
            alphabetical_letters.remove(letterGuessed)
    alphabetical_letters_remaining = "".join(alphabetical_letters)
    return alphabetical_letters_remaining

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))
