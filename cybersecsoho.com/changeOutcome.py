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
oldPassword = form.getvalue('oldPassword')
newPassword = form.getvalue('newPassword')
repeatPassword = form.getvalue('repeatPassword')
	
db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'datebases',
	database = 'python')

cursor = db.cursor()
sql = "SELECT * FROM users WHERE userName ='"+str(userName).lower()+"'"

cursor.execute(sql)
results = cursor.fetchone()
print(results)

if newPassword != repeatPassword:
	print('<h2>Something went wrong</h2>')
	print('<p class="description">Uh no, something went wrong. Your password was not changed.</p>')			
	print('<form class="loginform" action="login.py" method="post">')
	print('<input type="hidden" id="userName" name="userName" value="'+str(userName)+'">')
	print('<input type="hidden" id="employee" name="employee" value="'+str(employee)+'">')
	print('<input type="hidden" id="password" name="password" value="'+str(results[2])+'">')
	print('</br> </br>')
	print('<input class= "submit" id= "form_button" type="submit" value="back to main menu">')
	print('</form>')

	
else:
	sql = "SELECT password FROM users WHERE userName= '"+str(userName)+"'"
	cursor.execute(sql)
	currentPassword = cursor.fetchall()

	if currentPassword[0][0] == oldPassword and newPassword == repeatPassword:
		sql2="UPDATE users SET password = '"+str(newPassword)+"' WHERE username = '"+str(userName)+"'"
		cursor.execute(sql2)
		db.commit()
		
		if employee == 'True':
			sql3= "SELECT users.userName, employees.firstName, employees.lastName FROM users JOIN employees ON users.userID=employees.empNumber WHERE users.userName = '"+str(userName)+"' "
			
			cursor.execute(sql3)
			names = cursor.fetchall()
	
		else:
			sql3= "SELECT users.userName, customers.firstName, customers.lastName FROM users JOIN customers ON users.userID=customers.customerNumber WHERE users.userName = '"+str(userName)+"' "
			
			cursor.execute(sql3)
			names = cursor.fetchall()
			
		print('<form class="loginform" action="login.py" method="post">')
		print('<input type="hidden" id="userName" name="userName" value="'+str(userName)+'">')
		print('<input type="hidden" id="employee" name="employee" value="'+str(employee)+'">')
		print('<h2>Password changed!</h2>')
		print('<h3 class="description">'+str(names[0][1])+' '+str(names[0][2])+' ,you have succesfully changed your password!</h3>')
		print('<input type="hidden" id="password" name="password" value="'+str(newPassword)+'">')
		print('</br> </br>')
		print('<input type="submit" class="description login" style="float:none;" value="Return to main aplication">')
		print('</form>')
		
			
with open('/var/www/cybersecsoho.com/page_end.html', 'r') as end:
	content = end.readlines()

for i in content:
	print(i.rstrip('\n'))
	
cursor.close()
db.close()


