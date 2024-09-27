#! /usr/bin/env python3
import mysql.connector
import cgi, cgitb
import os, glob, datetime

db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'datebases',
	database = 'python')

cursor = db.cursor()

sql= "SELECT packetDateTime, protocol, srcMac, info FROM incidents WHERE customerNumber=1 and protocol='ARP'"

cursor.execute(sql)
packets= cursor.fetchall()
			


dates = [lis[0] for lis in packets]



info = [inf[-1] for inf in packets]
idNumbers=[]	
for inf in info:
	items = inf.rstrip('"')
	items= items.split(' ')
	idNumber=items[-1]
	idNumbers.append(idNumber)

	
macAddress = [inf[2] for inf in packets]
print(macAddress)	
print(idNumbers)
	
if 
			

