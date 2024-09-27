#!/usr/bin/env python3
from datetime import date
import os
import glob


	
def consent(prompt):
	if prompt == 'play':
		string = 'would you like to know how old you are?(y/n)'
	elif prompt == 'future':
		string = 'Would you like to know how old you will be in a particular date? (y/n)'
	elif prompt == 'save':
		string = 'would you like to save your results to a file?(y/n)'
	elif prompt == 'old':
		string = 'would you like to save your previous results to a file?(y/n)'		
	answer = input(string)
	
	
	while not(answer== 'y' or answer== 'n'):
		print('I\'m sorry, i didn\'t understand a question, please try again.')
		answer= input('Would you like to know how old you will be in a particular year? (y/n)')

	if answer== 'n':
		valid = False
		
	else:
		valid = True
		
	return valid
	
def obtainDate(prompt):
	dateValid = False
	while dateValid is False:
		print('Valid format for dates: \'1/1/2000\' or \'1 jan, 2000\'')
		if prompt =='dob':
			string ='What is your birthday?'
		if prompt =='future':
			string ='What date did you want to know about?'
		date = input(string)
		dateValid = validDate(date)
		if bool(dateValid) is False:
			print('I\'m sorry that is not a valid date')
			print('')
			
		return date

def parseDate(date):	
	if date[0].isdigit() is True: 		
		tempDate = date.split('/')
		day = tempDate[0]
		year = tempDate[2]
		month = tempDate[1]
	else:
		tempDate =  date.split()
		day = tempDate[0]
		year = tempDate[2]
		month = ''
		for i in tempDate[1]:
			if i !=',':
				month = month + i
		month = convertMonth(month)
		
	return day, month, year

def convertMonth(month):
	months = ['jan', 'feb','mar', 'may', 'apr', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
	
	if month[0:3].lower() in months:
		month = months.index(month[0:3].lower())
	else: 
		month = 'notValid'
		return month
	return month

def validDate(date):
	dateValid = False
	dayValid = False
	monthValid = False
	yearValid = False
	longMonths = [1, 3, 5, 7, 8, 10, 12]
	shortMonths = [4, 6, 9, 11]
	
	if date[0].isdigit() is True:
		tempDate = date.split('/')
	else:
		tempDate = date.split()
	if len(tempDate) < 3:
		return dateValid
	day, month, year = parseDate(date)
	
	
	if month == 'notValid':
		return dateValid
	
	month = int(month)
	day = int(day)
	year = int(year)
	
	if month > 0 and month <=12:
		monthValid = True
	
	if month in longMonths: 
		if day <= 31 and day != 0:
			dayValid = True
	elif month in shortMonths: 
		if day <= 30 and day != 0:
			dayValid = True
	elif month == 2:
		if day <= 29 and day > 0:
			dayValid = True
	if year > 1900:
		yearValid = True
		
		
	if monthValid is True and dayValid is True and yearValid is True:
		dateValid = True
	return dateValid
	
def dateDifference(day, month, year):

	age = int(year[1]) - int(year[0])
		
	day[0] = int(day[0])
	day[1] = int(day[1])
	if int(month[1]) <= int(month[0]):
		age = age -1
		if month[1] == month[0]:
			if day[1] >=day[0]:
				age = age +1	

	return age

print('Welcome to the age calculator.')
valid = consent('play')


if valid is True:	
	dates = []
	month = ['', ''] #index 0 dla daty urodzenia index 1 dla przyszej daty
	day = ['', '']
	year = ['', '']
	
	dob = obtainDate('dob')
	dates.append(dob)
	
	month[0], day[0], year[0] = parseDate(dates[0])
	
	today = date.today()
	
	day[1] = today.day
	month[1] = today.month
	year[1] = today.year
	
	age= dateDifference(day, month, year)
	
	resultsToday = 'Today you are {} years old.'
	print(resultsToday.format(age))
	
	
	validSave = consent('save')	
			
	if validSave == True:
		
		if os.path.isfile('age.txt') is True:
			validOld= consent('old')
		else:
			validOld = False
		if validOld is True:
			with open('age.txt', 'r') as oldFile:
				oldContent = oldFile.read()
		if os.path.isfile('age.txt') is True:
			age_files = glob.glob('age*.txt')
			age_files2 = sorted(age_files, reverse=True)
			
			numOfAgeFiles = len(age_files)
			for i in age_files2:
				newFileName = 'age' + str(numOfAgeFiles) + '.txt'
				os.rename(i, newFileName)
				numOfAgeFiles -= 1
		print('Saving your results to age.txt')
		age_file = open('age.txt', 'w+')
		dobMsg = 'Your birthday is ' +str(dates[0])+ '.\n'
		todayMsg = 'Today is ' +str(today)+ '.\n'
		age_file.write(dobMsg)
		age_file.write(todayMsg)
		age_file.write(resultsToday.format(age))
		age_file.write('\n') #zapewnia ze kazda wiadmosc jest w nowym wierszu
		
		
	valid = consent('future')
	
	
	
while valid is True:
	future = obtainDate('future')
	if len(dates) == 1:
		dates.append(future)
	else:
		dates[1] = future

	day[1], month[1], year[1] = parseDate(dates[1])
	
	
	age = dateDifference(day, month, year)	

	results = 'On {} you will be {} years old'
	print(results.format(dates[1], age))
	
	if validSave is True:
		age_file.write(results.format(dates[1], age))
		age_file.write('\n')
	
	valid = consent('future')
	
	if validOld is True:
		age_file.write('\n')
		age_file.write('the contents of the previous  age.txt were: \n')
		age_file.write(oldContent)
		
	if validSave is True:
		age_file.close()	
print('I\'m sorry you are not interested. Goodbye!')

