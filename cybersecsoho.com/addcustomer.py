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
print('<title>Success</title>')
print('<link rel="icon" type="image/x-icon" href="images/favicon.ico">')
print('<link rel="preconnect" href="https://fonts.googleapis.com">')
print('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
print('<link href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,300..700;1,300..700&family=MedievalSharp&display=swap" rel="stylesheet">')
print('<link rel="stylesheet" href="css/main.css">')
print('<link rel="stylesheet" media="screen and (min-width: 0px) and (max-width: 700px)" href="css/mobile.css">')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">')
print('!--<link rel="stylesheet" type="text/css" media="screen and (min-width: 481px) and (max-width: 768px)" href="../css/flex/kolejny-css.css"> do roznych rozdizelczosci dopasowac elementy, dodając kolejny css-->')
print('</head>')

with open('/var/www/cybersecsoho.com/page_start.html','r') as start:
	content=start.readlines()
for i in content:
	print(i.rstrip('\n'))
	
form =cgi.FieldStorage()
firstName = form.getvalue('firstName')
lastName = form.getvalue('lastName')
companyName = form.getvalue('companyName')
address = form.getvalue('address')
city = form.getvalue('city')
state = form.getvalue('state')
zipCode = form.getvalue('zipCode')
email = form.getvalue('email')
telephone = form.getvalue('telephone')


	
db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'datebases',
	database = 'python')

cursor = db.cursor()

sql = 'INSERT INTO customers (firstName, lastName, companyName, address, city, state, zipCode, email, phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
value = (str(firstName), str(lastName), str(companyName), str(address), str(city), str(state), str(zipCode), str(email), str(telephone)) 

cursor.execute(sql, value)
db.commit()



sql = "SELECT customerNumber FROM customers WHERE firstName = '"+str(firstName)+"' AND lastName = '"+str(lastName)+"' AND companyName = '"+str(companyName)+"'"


cursor.execute(sql)
customerNumber = cursor.fetchone()
customerNumber = customerNumber[0]
#customerNumber = int(''.join(map(str, customerNumber)))




firstName = str(firstName)
lastName = str(lastName)

userName = firstName[0].lower()+lastName.lower()

sql = "INSERT INTO users (userID, userName, password, type) VALUES (%s, %s, %s, %s)"
value =(customerNumber, userName, 'P@ssw0rd', 'c')

cursor.execute(sql, value)
db.commit()

print('<h2>Application Successful!</h2>')
print('<p class=”description”>Your user name is: &quot;'+userName+'&quot; and your temporary password is: &quot;P@ssw0rd&quot;. You can click <a href="http://www.cybersecsoho.com/login.html" style="color: #474544;">here</a> to login.</p>') 

with open('/var/www/cybersecsoho.com/page_end.html', 'r') as end:
	content = end.readlines()

for i in content:
	print(i.rstrip('\n'))
	
cursor.close()
db.close()


