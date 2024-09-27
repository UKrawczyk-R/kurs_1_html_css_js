#! /usr/bin/env python3
import mysql.connector

db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'datebases',
	database = 'python'
)

cursor = db.cursor()

cursor.execute('SELECT * FROM users')
allusers = cursor.fetchall()

for i in allusers:
	print(i)

print('')
input()

cursor.execute('SELECT * FROM customers')
allcustomers = cursor.fetchall()

for i in allcustomers:
	print(i)

print('')
input()

cursor.execute('SELECT * FROM incidents')
allincidents = cursor.fetchall()

for i in allincidents:
	print(i)

print('')
input()
cursor.execute('SELECT * FROM employees')
allemployees = cursor.fetchall()

for i in allemployees:
	print(i)

print('')
input()

cursor.close()
db.close()


