from __future__ import print_function
import random

HANGMANPICS = ['''
 +---+
 |   |
     |
     |
     |
     |
=========''','''
 +---+
 |   |
 O   |
     |
     |
     |
=========''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''','''
 +---+
 |   |
[o   |
/|\  |
/ \  |
     |
=========''','''
 +---+
 |   |
[o]  |
/|\  |
/ \  |
     |
=========''']
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe manga strawberry tomato'.split(),
'Animals':'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret goat goose hawk lion lizard llama mole monkey moose mouse mule own panda parrot pigeon python rabbit ram rat raven  rhino salmon seal shark sheep skunk slot snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(wordDict):
    #This function returns a random string from 
    #the passed dictionary of lists of strings, and the key also.
    #First randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    #Second, randomly select a word from the key's list in the dictionary
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_'*len(secretWord)

    for i in range(len(secretWord)): #replace blanks with correct guesses
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #show the secret word spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #Returns the letter the player already entered.
    #This function makes sure the player enetered a single letter.
    while True:
        print('Guess a letter.')
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    #this function returns True if the player wants to play again, else False
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord, secretKey = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretKey)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the plater type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters,
                secretWord)
            print('You have run out of guesses!\nAfter ' 
                + str(len(missedLetters)) + ' missed guesses and '
                + str(len(correctLetters)) + ' correct guesses, the word '
                + 'was "' + secretWord + '"')
            gameIsDone = True

    # Ask if they want to playa gain (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretKey = getRandomWord(words)
        else:
            break
