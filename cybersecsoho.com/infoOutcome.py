#! /usr/bin/env python3

import mysql.connector
import cgi, cgitb


print('content-type:text/html')
print('')
print('')
print('')

print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<title>CyberSecSOHO Change Password</title>')
print('<link rel="icon" type="image/x-icon" href="images/favicon.ico">')
print('<link rel="preconnect" href="https://fonts.googleapis.com">')
print('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
print('<link href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,300..700;1,300..700&family=MedievalSharp&display=swap" rel="stylesheet">')
print('<link rel="stylesheet" href="css/main.css">')
print('<link rel="stylesheet" media="screen and (min-width: 0px) and (max-width: 700px)" href="css/mobile.css">')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">')

print('</head>')

with open('/var/www/cybersecsoho.com/page_start.html','r') as start:
	content=start.readlines()
for i in content:
	print(i.rstrip('\n'))
	
form =cgi.FieldStorage()
userName = form.getvalue('userName')
employee = form.getvalue('employee')
password = form.getvalue('password')
companyName = form.getvalue('companyName')
address = form.getvalue('address')
city = form.getvalue('city')
state= form.getvalue('state')
zipCode= form.getvalue('zipCode')
email= form.getvalue('email')
phone= form.getvalue('phone')
	
db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'datebases',
	database = 'python')

cursor = db.cursor()

print(userName, employee, password, companyName, address, city, state, zipCode, email, phone)

sql="UPDATE customers SET companyName = '"+str(companyName)+"',address = '"+str(address)+"',city = '"+str(city)+"',state = '"+str(state)+"' ,zipCode = '"+str(zipCode)+"',email = '"+str(email)+"',phone = '"+str(phone)+"'WHERE lastName = '"+userName[1:].title()+"'"
cursor.execute(sql)
db.commit()

sql3= "SELECT users.userName, customers.firstName, customers.lastName FROM users JOIN customers ON users.userID=customers.customerNumber WHERE users.userName = '"+str(userName)+"' "

cursor.execute(sql3)
names = cursor.fetchall()
			
print('<form class="loginform" action="login.py" method="post">')
print('<input type="hidden" id="userName" name="userName" value="'+str(userName)+'">')
print('<input type="hidden" id="employee" name="employee" value="'+str(employee)+'">')
print('<input type="hidden" id="password" name="password" value="'+str(password)+'">')
print('<h2>Contact information updated!</h2>')
print('<h3 class="description">'+str(names[0][1])+' '+str(names[0][2])+', you have succesfully changed your contact information!</h3>')
print('</br> </br>')
print('<div class="submit">')
print('<input type="submit" value="Return to main aplication" id="form_button" />')
print('</div>')
print('</form>')

			
with open('/var/www/cybersecsoho.com/page_end.html', 'r') as end:
	content = end.readlines()

for i in content:
	print(i.rstrip('\n'))
	
cursor.close()
db.close()

