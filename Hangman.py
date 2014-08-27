#Hangman.py
#Tech Kuo
#June 29th 2014

import getpass
import random
import re

"""
==========
Hangman
==========
Module that allows you to play Hangman in your command prompt.
To play the game with its amazing ASCII graphics, simply run hangman.py.

Rules are about what you would expect in a game of Hangman. Only thing that
might be of note is that players have 5 chances/lives/body parts to guess with.

There are two modes : single player and two player.

Single player lets the computer randomly chooses a word for you to guess
and supplies you with a hint in order to get you started.

Two player requires one player to type a word in to serve as the word 
being guessed at the beginning and another player to guess what the word is.


"""

HANGMANDISPLAY = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

ANIMALS = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
COLORS = 'red blue green yellow white black orange purple pink brown violet gold silver gray maroon cyan lavender magenta indigo cerulean tan turqoise scarlet sepia teal  '.split()
FRUITS = 'apple apricot banana blackberry blueberry cantaloupe cherry coconut cranberry date dragonfruit durian grape grapefruit guava honeydew jackfruit kiwi lemon lime lychee mango watermelon nectarine papaya passionfruit peach pear plum pineapple pomegranate raspberry strawberry orange'.split()
wordArray = [ANIMALS, COLORS, FRUITS]
hintArray = ['animals', 'colors', 'fruits']

answer = ''
blankList = []
guess = ''
missedLetters = ''
hint = ''
singlePlayer = True 
gameFinished = False
playAgain = True

def displayState() :
    print HANGMANDISPLAY[len(missedLetters)] 
    print "Secret Word : " + ' '.join(blankList)
    print "Missed Letters : " + ",".join(missedLetters)

def CheckNumPlayers() :
    global singlePlayer
    answer = raw_input("\nPlease state the number of players. 1 or 2 : ")
    if (answer == '1'):
        singlePlayer = True
    elif (answer == '2'):
        singlePlayer = False
    else:
        print "Not a valid input. Try again."
        CheckNumPlayers()

def getRandomWord():
    global wordArray
    global hintArray
    global hint
    global answer
    listIndex = random.randint(0,2)
    wordBank = wordArray[listIndex]
    wordIndex = random.randint(0, len(wordBank)-1)
    hint = hintArray[listIndex]
    answer = wordBank[wordIndex]

def handleAnswer() :
    global blankList
    global answer
    global singlePlayer
    if singlePlayer == True:
        getRandomWord()
        print "The hint is " + hint
    else: 
        answer = getpass.getpass('\nPlease enter the word to be guessed: ').lower()
        if not(re.match("[a-z]+",answer)):
            print "\nInvalid word. No special or whitespace characters allowed."
            handleAnswer()
    blanks = '_' * len(answer)
    blankList = list(blanks)
    displayState()

def handleGuess() :
    global missedLetters
    global blankList
    global guess
    guess = raw_input('\nPlease guess a letter: ').lower()
    if (len(guess) > 1):
        print 'Invalid guess. Only a SINGLE letter input is accepted.'
        handleGuess()
    if (guess not in 'abcdefghijklmnopqrstuvwxyz'):
        print 'Invalid guess. No special characters allowed.'
        handleGuess()
    if ((guess in missedLetters) or (guess in blankList)):
        print 'The letter has already been guessed. Guess again.'
        handleGuess()
    for i in range(len(answer)):
        if (guess == answer[i]) :
            blankList[i] = guess
    if(not(guess in answer)):
        missedLetters+=guess
    displayState()

def checkState() :
    global gameFinished
    if (len(missedLetters) == 5): 
        gameFinished = True
        print "\nYou have run out of guesses. Game Over."
        print "The answer was " + answer
    elif not('_' in blankList):
        gameFinished = True
        print "\nYou win! Congratulations!"
    else:
        gameFinished = False

def playGame() : 
    global gameFinished
    handleAnswer()
    while (gameFinished == False) :
        handleGuess()
        checkState()

def CheckPlayAgain() :
    global playAgain
    global gameFinished
    global missedLetters
    answer = raw_input("\nWould you like to play again? y or n : ")
    if (answer == 'y') : 
        playAgain = True
        gameFinished = False
        missedLetters = ''
    elif (answer == 'n') :
        playAgain = False
    else :
        print "Invalid input. Please try again."
        CheckPlayAgain()

print "< - - - H A N G M A N - - - >"
print "-----------------------------"
print "--------by Tech Kuo----------"
print "-----------------------------"
while playAgain == True:
    CheckNumPlayers()
    playGame()
    CheckPlayAgain()