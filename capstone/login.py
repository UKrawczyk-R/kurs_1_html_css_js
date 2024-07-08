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
print('<title>CyberSecSOHO app</title>')
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
userName = form.getvalue('UserName')
password = form.getvalue('password')
employee = form.getvalue('employee')
	
db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'datebases',
	database = 'python')

cursor = db.cursor()

sql = "SELECT * FROM users WHERE userName ='"+str(userName).lower()+"' AND password = '"+str(password)+"'"

cursor.execute(sql)
results = cursor.fetchall()

if len(results) == 1:
	print('<form class="loginform" action="main.py" method="post">')
	print('<input type="hidden" id="userName" name="userName" value="'+str(userName)+'">')
	if employee == 'employee':
		print('<input type="hidden" id="employee" name="employee" value="True">')
	else:
		print('<input type="hidden" id="employee" name="employee" value="False">')
	print('<input type="submit" style="background: none; border: none; color: #474544; text-decoration: underline; cursor: pointer; font-size: 250%;" value="Click here to go to main app">')
	print('</form>')
else:
	print('<h2 class="heading">Authentication Failed</h2>')
	print('<p class="description">Click <a href="http://www.cybersecsoho.com/login.html" style="color;  color: #474544; text decoration: none;">here</a> to retry.</p>')	

with open('/var/www/cybersecsoho.com/page_end.html', 'r') as end:
	content = end.readlines()

for i in content:
	print(i.rstrip('\n'))
	
cursor.close()
db.close()


