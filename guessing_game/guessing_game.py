#!/usr/bin/env python3
import random 

#initialize variables.
wrongGuesses = 7
guessed = False
corectLetters = []
wrongLetters = []
blanks = ''

with open('wordlist.txt', 'r') as words:
	tempList = words.readlines()
	


words = []

for word in tempList:
	words.append(word.rstrip('\n'))

indexNumber = random.randint(0, (len(words)-1))	# -1 poniewaz lista zaczyna si od 0
	
def processGuess(turn, guess, wrongGuesses):
	blanks =''
	validLetter = False

	if guess in word:
		validLetter = True
		
	if validLetter ==True:
		if turn != 1:
			corectLetters.append(guess)
			print('correct!', 'The letter', guess, 'is in the word.')
		
	else:
		if turn != 1:
			wrongLetters.append(guess)
			wrongGuesses = wrongGuesses - 1
			print('I\'m sorry,', guess, 'is not in the word.')
		print('You have', wrongGuesses, 'worng guesses left.')
		
	lettersGuessedCorect = 0		
	for i in word:
		letterInWord = False
		if i in corectLetters:
			letterInWord = True
			lettersGuessedCorect = lettersGuessedCorect + 1
				
		if letterInWord is True:
			blanks = blanks + i + ' '
		else:
			blanks = blanks + '_ '
			
	print(blanks)
	return lettersGuessedCorect, wrongGuesses
	
word = words[indexNumber]
	
processGuess(1, '', wrongGuesses)
turn = 2

while guessed is False and wrongGuesses > 0:
	
	print('Corect Letters Guessed: ', corectLetters)
	print('wrong Letters guessed: ', wrongLetters)
	
	guess = input('what letter would you like to guess? ').lower()
	
	
	newLetter = True
	if guess in wrongLetters:
		newLetter = False
	if guess in corectLetters:
		newLetter = False
			
	if newLetter is False:
		print('I\'m sorry, you already guessed that letter')
		continue
	elif guess.isdigit() is True:
		print('I\'m sorry, you can only guess letters')
		continue
	
		
	lettersGuessedCorect, wrongGuesses = processGuess(turn, guess, wrongGuesses)		
		
		
	if len(word) == lettersGuessedCorect:
		print('you have guessed the word! You had', wrongGuesses, 'wrong guesses left.')
		guessed = True

	
	
if wrongGuesses == 0:
	print('Too bad! The word was:', word)
	print('I\'m sorry you lose')
else:
	print('Congratulations! You win!')

	print('Please play again!')




