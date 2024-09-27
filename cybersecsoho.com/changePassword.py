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
	
db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'datebases',
	database = 'python')

cursor = db.cursor()

sql = "SELECT * FROM users WHERE userName ='"+str(userName).lower()+"'"

cursor.execute(sql)
results = cursor.fetchone()

if employee == 'True':
	sql2 = "SELECT firstName, lastName FROM employees WHERE empNumber ='"+str(results[0])+"'"

	cursor.execute(sql2)
	names = cursor.fetchall()
	
	print('<div id="container_form">')
	print('<form action="changeOutcome.py" method="post">')
	print('<input type="hidden" id="userName" name="userName" value="'+str(userName)+'">')
	print('<input type="hidden" id="employee" name="employee" value="True">')
else:
	sql2 = "SELECT firstName, lastName FROM customers WHERE customerNumber ='"+str(results[0])+"'"

	cursor.execute(sql2)
	names = cursor.fetchall()
	
	print('<div id="container_form">')
	print('<form action="changeOutcome.py" method="post">')
	print('<input type="hidden" id="userName" name="userName" value="'+str(userName)+'">')
	print('<input type="hidden" id="employee" name="employee" value="False">')
	
print('<h3 class="header">'+str(names[0][0])+' '+str(names[0][1])+'</h3>')
print('<h3 class ="users">UserName: '+str(userName)+'</h3></br></br>')

print('<div class="name  login_form " style="float:none;">')
print('<label for="oldPassword"></label>')
print('<input placeholder="Old password" required="required" size="25" type="password" id="oldPassword" name="oldPassword" />')
print('<label for="newPassword"></label>')
print('<input placeholder=" New password" required="required" size="25" type="password" id="newPassword" name="newPassword" />')
print('<label for="repeatPassword"></label>')
print('<input placeholder="repeat new password" required="required" size="25" type="password" id="repeatPassword" name="repeatPassword" />')
print('</div>')
print('<div class="submit">')
print('<input id="form_button" type="submit" value="Change Password" />')
print('</div>')


with open('/var/www/cybersecsoho.com/page_end.html', 'r') as end:
	content = end.readlines()

for i in content:
	print(i.rstrip('\n'))
	
cursor.close()
db.close()


