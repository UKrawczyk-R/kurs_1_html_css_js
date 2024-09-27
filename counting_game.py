#!/usr/bin/env python3

#Function to promt user.
#If user answers no, if this is a first time, the users plays, deliver one message
#If user has alredy played a round, dleiuver a diffrent message.
#in either case, set game to True.


#play function will be prompt the user and analized the answers
def play(prompt, gameOver):
	#string used to build a prompt.
	text = 'Would you like to analyze {} number? (y/n)'
	
	#if first round, use 'a'
	#if additional rounds use 'another'
	if prompt == 1:
		det = 'a'
	else:
		det = 'another'
	
	#prompt user for choice using formatted text variable
	answer = input(text.format(det))
	
	#while loop to process user input
	#loop will execute unless the user enters y, Y, n or N.
	
	while not(answer.lower() == 'y' or answer.lower() == 'n'):
		print('I\'m sorry, i didn\'t understand, please try again.')
		print('')
		answer = input(text.format(det))
	# if statment to handle 'n' response.
	if answer.lower() == 'n':
		#set gemeOver variable to True
		gameOver = True
		
		#if the first round, print one message.
		#if not the first round, print a diffrent message.
		
		if prompt == 1:
		
			print('That\'s too bad, we could have had fun.')
			print('')
			return prompt, gameOver
		else:
		 	print('No worries. Thanks you  for the playing!')
		 	print('')
		 	return prompt, gameOver
	#else to process 'y' responce.
	#incremante prompt to indicate another round has started
	else:
		prompt += 1
		
	#return statement returns the changed values of prompt and gameOver
		return prompt, gameOver
	
#function to ask the user for a number.

def getNumber():
	#valid variable to test user input.
	#starrts as False.
	valid = False
	
	#while loop to get and process input.
	while valid is False:
		#ask user to enter a number
		numberInput = input('Please eneter a number between 1 and 10: ')
		
		#if the user eneter a non numeric response
		#return message and move on to the next iteraion
		if numberInput.isdigit() is not True:
			print('I\'m sorry, i need a number')
			print('')
			continue # break the loop and skip to the next iteration(top of the loop)
		# if the user entered a numeric responce below  1 or above 10
		#print message and move on to next iteration.
		
		elif int(numberInput) == 0 or int(numberInput) > 10:
			print('I\'m sorry, the number must be betwwen 1 and 10.')
			print('')
			continue # break the loop and skip to the next iteration
		#else runs if responce was number betwwen 1-10
		else:
			valid = True
			
	# return the number to the main app
	return numberInput
	
# function to process the number
def processNumber(number):
	#change the string to an integer
	number = int(number)
	
	#if ....elif....else statement
	if number == 10:
		print('high roller!')
	elif number >= 8:
		print('you like your numbers hight!')
	elif number >= 4:
		 print('a middle of the roud guy, huh?')
	else:
		 print('keeping it small, i like it!')
	print('')
	print('')

#main application begins.
#statements to initialize the 3 variables

prompt = 1
gameOver = False
number = ''

#while loop continues game play as long as the user does not answer 'n' when asked to play a game

while gameOver is False:
	# call the play function with the prompt, gameOver variables
	#store updated values in the orginal variables
	
	prompt, gameOver = play(prompt, gameOver)# nnowe artoc		 
	
	# if the user said 'n' break the loop whitch ends the game
	if gameOver is True:
		break
	# if the user did not say no, call the getNumber() function store the results in the number variable
	number = getNumber()
	
	#then call the processNumber function sending the number as the argument.
	processNumber(number)
	
		
	
