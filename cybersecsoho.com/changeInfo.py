#! /usr/bin/env python3
import mysql.connector
import cgi, cgitb

print('Content-type:text/html')
print('')
print('')
print('')

print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<title>CyberSecSOHO update info</title>')
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
password = form.getvalue('password')
employee = form.getvalue('employee')
	
db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'datebases',
	database = 'python')

cursor = db.cursor()

sql=" select companyName, address, city, state, zipCode, email, phone FROM customers where lastName = '"+userName[1:].title()+"'"

cursor.execute(sql)
customersData = cursor.fetchall()



print('<h3 class ="users">UserName:  '+str(userName)+'</h3>')
print('<div id="container_form">')
print('<form action="infoOutcome.py" method="post">')

print('<div class="name login_form">')


print('<label for="companyName_input"></label>')
print('<input type="text" placeholder="company Name" name="companyName" id="companyName_input" value="'+customersData[0][0]+'"required>')
print('<label for="address_input"></label>')
print('<input class="register" type="text"  placeholder="address" name="address" id="address_input" value="'+customersData[0][1]+'"required>')
print('<label for="city_input"></label>')
print('<input type="text" placeholder="city" name="city" id="city_input" value="'+customersData[0][2]+'" required>')
print('</div>')
print('<div class="email">')

print('<label for="state_input"></label>')
print('<input type="text" placeholder="state (example:PL)" name="state" id="state_input" value="'+customersData[0][3]+'"required>')
print('<label for="zipCode_input"></label>')
print('<input type="text" placeholder="zip code(00000)" name="zipCode" id="zipCode_input" pattern="[0-9]{5}" value="'+customersData[0][4]+'" required>')
print('<label for="email_input"></label>')
print('<input class="register" type="email" placeholder="e-mail" name="email" id="email_input" value="'+customersData[0][5]+'"required>')
print('<label for="telephone_input"></label>')
print('<input type="text" placeholder="telephone 00 000 000 000" name="telephone" id="telephone_input" value="'+customersData[0][6]+'" pattern="^\d{2} \d{3}( |-)?\d{3}( |-)?\d{3}( |-)?$">')
print('</div>')
print('<input type="hidden" id="employee" name="employee" value="False">')
print('<input type="hidden" id="userName" name="userName" value="'+str(userName)+'">')
print('<input type="hidden" id="password" name="password" value="'+str(password)+'">')
print('<div class="submit">')
print('<input type="submit" value="Update information" id="form_button" />')
print('</div>')
print('</form>')

with open('/var/www/cybersecsoho.com/page_end.html', 'r') as end:
	content = end.readlines()

for i in content:
	print(i.rstrip('\n'))
	
cursor.close()
db.close()


