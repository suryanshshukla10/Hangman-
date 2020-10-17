# Hangman game
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    LsecretWord = list(secretWord)
    #if len(LsecretWord) != len(lettersGuessed):
     #   return False
    sw = LsecretWord[:]
    for e in lettersGuessed:
     #   print(e)
        if e in sw:
            #print(LsecretWord)
            sw.remove(e)
    if sw == [] :
        return True
    else:
        return False
                



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    sw = list(secretWord)
    newList = []
    swC = sw[:]
    LGC = lettersGuessed[:]
    y = len(sw)
    newList = ['_']
    newList = y * newList
    for e in LGC:
        counts = swC.count(e)
        for i in range(counts):
            if e in swC:
                i = swC.index(e)
                newList[i] = e
                swC[i] = '*'
   
    newList = ''.join(newList)
    return (newList)
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    List = list(lettersGuessed)
    Y = string.ascii_lowercase
    y = list(Y)
    for e in List:
        if e in List:
            y.remove(e)
    z = ''.join(y)
    return z
    
    
    
    

def hangman(secretWord):
    print(secretWord)
    def line():
        print('-------------')
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', str(len(secretWord)) ,'letters long.')
    line()
    lettersGuessed = []
    stdList = []
    i = 8
    secretList = list(secretWord)
    while (i>0 and isWordGuessed(secretWord, lettersGuessed) == False):
        print('You have ' + str(i) +  ' guesses left.')
        print('Available letters: ', getAvailableLetters(stdList))
        lg = input('Please guess a letter: ')
        lg = lg.lower()
        if lg in stdList:
            print('Oops! You\'ve already guessed that letter: ', getGuessedWord(secretWord,lettersGuessed))
        else :
            stdList.append(lg)
            if lg in secretList:
                lettersGuessed.append(lg)
                print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
            else :
                print('Oops! That letter is not in my word: ', getGuessedWord(secretWord,lettersGuessed))
                i -= 1
        line()
    if i == 0:
        print('Sorry, you ran out of guesses. The word was ', secretWord)
    else:
        print('Congratulations, you won!')
    
    



hangman('y')


    







