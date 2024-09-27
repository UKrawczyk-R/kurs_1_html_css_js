#!/usr/bin/env python3

from random import randint

def startGame():
	print('The weather is hot and you are broke.\nwith only $1 left in your pocket,\nthe only thing you can do is start a lemonade stand.')
	answer=input('interested? (y/n)?')
	while len(answer) == 0:
		print("Please enter 'y' or 'n'.")
		answer=input('interested? (y/n)?')
		
	else:
		answer = answer[0].lower()
		
	while not(answer == 'y' or answer == 'n'):
		print('It\'s not a huge decision:')
		print('you either want start a lemonade stand')
		print('or you don\'t')
		answer = input('interested? (y/n)?')
	
	#extraxt only the first character in lower case	
	
	if answer== 'n':
		
		print('Totally understandable. The small buisness life isn\'t for everyone.\nIt ends where it started. you still have $1. No harm done.')
		
		quit = True
		return quit
	else:
		print('fantastic! Get out some posterboards and markers\nand get ready to triumph!')
		quit = False
		print()
		print('Press enter to continue...')
		input()
		
		return quit
	
def rules():
	rules=['Each day You will receive a forecast.', 'Based on the forecast, decide how much lemonade to make.', 'Weather, Temperature and price affect sales.','A heat wave will automatically sell all lemonade on hand.', 'A thunderstorm means no sales at all.']
	print()
	print('the rules are simple:')
	for rule in rules:
		print(rule)
	print()	
	print('press enter to continue...')
	input()

	
def new_day():
	global day
	forecast = ['heat wave', 'thunderstorm', 'sunny', 'cloudy']			
	
	
	sunny = randint(1,100)
	if sunny < 100:
		maxCloudy = 100 - sunny
		cloudy = randint(1, maxCloudy)
		maxHeatWave = 100 - sunny - cloudy
		if maxHeatWave > 0:
			heatWave = randint(1, maxHeatWave)
		else:
			heatWave = 0
	else:
		cloudy = 0
		heatWave = 0
	thunderstorm = 100 - sunny - cloudy - heatWave 
	
	weights=(sunny, cloudy, heatWave, thunderstorm)
	
	choices =(forecast, weights)
	
	weather = choices
	
	weather = weather[0]
	lemonade_cost = randint(1,10)
	temperature = randint(15, 40)
		
	day +=1
	
	return weather, lemonade_cost, temperature, sunny, cloudy, heatWave, thunderstorm

def forecast(lemonade_cost, temperature, sunny, cloudy, heatWave, thunderstorm):
	global day
	print()
	print('Day'+ str(day)+':')
	print('The temperature tomorrow is expected to be ' +str(temperature)+' degrees.')
	print()
	print('There is a '+str(sunny)+'% chance of being sunny,')
	print('a '+str(cloudy)+ '% chance of being cloudy,')
	print('a '+str(heatWave)+ '% chance of a heat wave,')
	print('a '+str(thunderstorm)+ '% chance of a thunderstorm.')
	print()
	print('The cost to make lemonade today is '+str(lemonade_cost)+' cents.')
	print()
	print('press enter to continue...')
	input()

def main_menu():
	menu =['1: Sell lemonade','2: Make lemonade','3: Close for the day','4: Forecast','5: Rules','6: quit']
	for i in menu:
		print(i)
	answer_menu= input('What do you want to do?')
			
	while answer_menu.isdigit() is False:
		print('please enter a number 1,2,3,4,5,6, or 7.')
		answer_menu= input('What do you want to do?')
	answer_menu = int(answer_menu)
	return answer_menu
		
	
			
def selling_lemonade(weather, inventory, temperature):
	print()
	print('maximum price: $1 (100cents)')
	print()
	sold_price= input('How many cents do you want to charge per cup?')
	if sold_price.isdigit() is True:
		sold_price = int(sold_price)
		
	while sold_price not in range(1, 101, 1):
		print('I\'m sorry, that\'s nota valid price.')
		print('Valid price are in cents from 0 to 100.')
		sold_price= input('How many cents do you want to charge per cup?')
		if sold_price.isdigit() is True:
			sold_price = int(sold_price)
			
	
	if weather == 'heatWave':
		demand == inventory
	elif weather =='thunderstorm':
		demand = 0
	else:
		cupsSold = randint(1, 100)
		priceFactor = float(100-sold_price)/100
		# 10% less demand for each 10 sent price incrise	
		heatFactor = 1 -(((40-temperature)*2)/float(100))
		# 20% less demand for each degree  under 100
		demand = (cupsSold*priceFactor*heatFactor)

	if weather == 'sunny':
		demand = demand*1.1
	elif weather == 'cloudy':
		demand = demand*.9
	demand = int(round(demand, 0))
			
		
	if demand < inventory:
		cupsSold = demand
	elif demand >= inventory:
		cupsSold = inventory
		
	if weather == 'Thunderstorm':
		print('Unfortunately, a thunderstorm kept you closed!')
	elif weather == 'heatWave':
		print('You have sold out thanks to a heat wave!')
	elif inventory == 0:
		print('You had 0 cups in inventory! No less, no gain.')
	elif cupsSold > inventory:
		print('You had '+str(inventory)+ ' cups in inventory!')
		print('You sold out!')
		print()
		print('But there was demand for '+str(demand)+' cups.')
		print('Next time you might want to have more inventory on hand.')
	elif cupsSold == inventory:
		print('You had '+str(inventory)+ ' cups in inventory!')
		print('There was demand for '+str(demand)+' cups.')
		print()
		print('You sold out!')
		print()
		print('Clearly you have a great mind for buisness!')
	elif cupsSold < inventory:
		print('You had '+str(inventory)+ ' cups in inventory!')
		print('There was demand for '+str(demand)+' cups.')
		print()
		print('Not a great sales day, but there\'s always tomorrow')
	return cupsSold, sold_price
		
	

def make_lemonade(cash, inventory, lemonade_cost):
	print('The cost to make lemonade today is '+str(lemonade_cost)+ ' cents.')
	print('Total cash on hand is: '+str(cash)+' cents.')
	print()
	lemonade_maked = input('How many cups of lemonade do you want to make? ')
	
	while lemonade_maked.isdigit() is False:
		print('please enter a number')
		lemonade_maked = input('How many cups of lemonade do you want to make? ')

	total_lemonade_cost = int(lemonade_maked)*int(lemonade_cost)
	print(cash, 'cash')
	print(total_lemonade_cost, 'cost')
	while int(total_lemonade_cost) > cash:
		print('You have not enough money to buy '+str(lemonade_maked)+ ' cups.')
		lemonade_maked = input('How many cups of lemonade do you want to make? ')
		total_lemonade_cost = int(lemonade_maked)*int(lemonade_cost)
		print(cash, 'cash')
		print(total_lemonade_cost, 'cost')
		
	inventory =int(inventory) + int(lemonade_maked)
	cash = cash - total_lemonade_cost
	print('you have made '+str(lemonade_maked)+' cups of lemonade')
	print('at total cost of of '+ str(total_lemonade_cost)+' cents.')
	print()
	print('Cups of lemonade in inventory: '+str(inventory))
	print('Total cash on hand is now: '+str(cash))
	print()
	print('press enter to continue...')
	input()
	
	return lemonade_maked, cash, total_lemonade_cost, inventory
	
def calculate_profits(cupsSold, sold_price, cash, inventory):
	
	profit = round(cupsSold*sold_price, 0)
	
	cash = cash + profit
	
	print()
	print('You sold '+str(cupsSold)+' cups of lemonade.')
	print('you total profit was '+str(profit)+' cents.')
	print()
	print('Total cash on hand is now '+str(cash)+' cents')
	print('Unsold lemonade is gone')
	inventory = 0
	print()
	print('press enter to continue...')
	input()
	return cash, inventory
	
	
		
	

quit = startGame()
if quit == False:
	rules()
day = 0
cash = 100
lemonade = 0
inventory = 0	
demand = 0
cupsSold = 0
sold_price = 0

while quit is False:
	weather, lemonade_cost, temperature, sunny, cloudy, heatWave, thunderstorm = new_day()
	forecast(lemonade_cost, temperature, sunny, cloudy, heatWave, thunderstorm)
	
	answer_menu = main_menu()
	while not(answer_menu==6 or answer_menu==3 or answer_menu==1): 	
		
			
		if answer_menu == 2:
			lemonade_maked, cash, total_lemonade_cost, inventory= make_lemonade(cash, inventory, lemonade_cost)
				
		elif answer_menu == 4:
			forecast(lemonade_cost, temperature, sunny, cloudy, heatWave, thunderstorm)
			
		elif answer_menu == 5:
			rules()
		answer_menu = main_menu()
	if answer_menu == 1:
			cupsSold, sold_price = selling_lemonade(weather, inventory, temperature)
			inventory = inventory - cupsSold
			cash, inventory = calculate_profits(cupsSold, sold_price, cash, inventory)		
	if answer_menu == 6:
		if day == 1:
			quit = True
			
		else:
			print('Total cash on hand is now: '+str(cash)+ 'cents')
			quit=True
			
	elif answer_menu == 3:
		cash, inventory = calculate_profits(cupsSold, sold_price, cash, inventory)
else:	
	total_profit = cash - 100
	if total_profit > 0:
		print("Wow, you increased your net worth by "+str(total_profit))
		print("You're well on your way to being rich!")
		print("If you're ever broke again, you can always sell lemonade!")
	elif total_profit == 0:
		print("It ends where it started. You still have $1. No harm done.")
	elif total_profit < 0:
		print("Maybe sales is not your thing.")
		print("You lost "+str(total_profit * -1)+" cents.")
		print("You should probably get looking for a job.")
		print("It's going to be a long road to paying back your parents.")

	print()
	print('Goodbye')
	
