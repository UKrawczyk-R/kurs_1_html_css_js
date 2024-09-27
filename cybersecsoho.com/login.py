#! /usr/bin/env python3
import mysql.connector
import cgi, cgitb
import os, glob, datetime


def processLog():
	logFiles = glob.glob('/var/www/cybersecsoho.com/logs/*.csv')

	newIncidents=[]
		
	if len(logFiles)>=1:
		
		
		for file in logFiles:
			with open(file, 'r') as current:
				tempList = current.readlines()
			newIncidents.append(tempList)
			
			nameParts = file.split('/')
			fileParts = nameParts[-1].split('_')
			
			customerNumber = fileParts[0]
			moreParts = nameParts[-1].split('.')
			newFileName='/var/www/cybersecsoho.com/logs/'+moreParts[0]+str(datetime.date.today())+'.old'
			os.rename(file, newFileName)
			
			
			counter = 0
			for file in newIncidents:
				counter = 0
				for incident in file:
					if counter ==0:
						counter+=1
						continue
					items=incident.split(',')
					itemCounter = 0
					
					for item in items:
						items[itemCounter]=item.strip('"')
						itemCounter +=1
					items[-1] = items[-1].rstrip('\n')
					items.append(customerNumber)
					
					sql = "INSERT INTO incidents(packetDateTime, srcIP, destIP, protocol, srcPort, destPort, hostIP, serverIP, srcMac, destMac, info, customerNumber) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
					values=(items[1], items[2], items[3], items[4],items[6],items[7],items[8],items[9],items[10],items[11],items[12],int(items[13]))
				
					cursor.execute(sql, values)
					db.commit()
#end def processlog
def synFlood(customerNumber):
	sql= "SELECT packetDateTime, srcIP,destIP, info, destPort FROM incidents WHERE customerNumber='"+str(customerNumber)+"'"

	cursor.execute(sql)
	packets= cursor.fetchall()
				

	badPackets=[]
	for packet in packets:
		if packet[1] ==packet[2] and packet[3].find('[SYN]') != -1:
			badPackets.append(packet)
	datePorts= dict()
	for badPacket in badPackets:
		if badPacket[0] not in datePorts:
			datePorts[badPacket[0]] = {badPacket[4]:1}
		else:
			if badPacket[4] not in datePorts[badPacket[0]]:
				datePorts[badPacket[0]][badPacket[4]] = 1
			else:
				oldValue= datePorts[badPacket[0]][badPacket[4]]
				newValue = oldValue+1
				datePorts[badPacket[0]][badPacket[4]]= newValue				
	return datePorts
#endDef synFlood

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
processLog()

sql = "SELECT * FROM users WHERE userName ='"+str(userName).lower()+"' AND password = '"+str(password)+"'"

cursor.execute(sql)
results = cursor.fetchall()



if len(results) == 1: #if record will return form the table
#tworzymy formularz na stronie ktrory bedzie zawieral informacje oraz hiperacze,kotre przesyla informacje do nastepnego skryptu
	
	lastName = ''
	for i in userName:
		lastName = lastName + i
	lastName = lastName[1:]
	
	
	if employee == 'Employee':
		
		sql ="SELECT * FROM employees WHERE empNumber = '"+str(results[0][0])+"' AND lastName = '"+str(lastName.title())+"'"
		cursor.execute(sql)
		userRecord = cursor.fetchone()
		if userRecord is None:
			print('<h2>&bull;Something Went Wrong&bull;</h2>')
			print('<p class="description">Uh no, something went wrong. If you are an employee, make sure you chcecked the employee box on login page. If you not, please do not check the box.</p>')
			print('<p class="description login">Click <a href="login.html">here</a> to retry.</p>')
		else:	
			print('<h3 class="header">'+str(userRecord[1])+' '+str(userRecord[2])+'</h3>') 
			print('<div class="users">')
			print('<h3>'+str(userRecord[4])+'</h3>')
			print('<h3>Email: '+str(userRecord[3])+'</h3>')
			print('<h3 >UserName: '+str(userName)+'</h3>')
			print('</div>')
			print('<form class="loginform" action="changePassword.py" method="post">')
			print('<input type="hidden" id="userName" name="userName" value="'+str(userName)+'">')
			print('<input type="hidden" id="employee" name="employee" value="True">')
			print('</br> </br>')
			print('<input class= "submit" id= "form_button" type="submit" value="Change Password">')
			print('</form>')
			
			
	else:
		sql ="SELECT * FROM customers WHERE customerNumber = '"+str(results[0][0])+"' AND lastName = '"+str(lastName.title())+"'"
		cursor.execute(sql)
		userRecord = cursor.fetchone()
		if userRecord is None:
			print('<h2>&bull;Something Went Wrong&bull;</h2>')
			print('<p class="description">Uh no, something went wrong. If you are an employee, make sure you chcecked the employee box on login page. If you not, please do not check the box.</p>')
			print('<p class="description login">Click <a href="login.html">here</a> to retry.</p>')
		else:	

		
			print('<div class="customer" style="width:fit-content; float: left;">')
			print('<h3 class="header">'+str(userRecord[1])+' '+str(userRecord[2])+'</h3>') 
			print('<div class="users">')
			print('<h3>Company Name: '+str(userRecord[3])+'</h3>')
			print('</div>')
			print('</div>')
			print('<form  style="padding:5px;" action="changePassword.py" method="post">')
			print('<input type="hidden" id="userName" name="userName" value="'+str(userName)+'">')
			print('<input type="hidden" id="password" name="password" value="'+str(password)+'">')
			print('<input type="hidden" id="employee" name="employee" value="False">')
			
			print('<input class= "submit" id= "form_button" type="submit"  style="float:right;" value="Change Password">')
			print('</form>')
			
			print('<form style="padding:5px;" action="changeInfo.py" method="post">')
			print('<input type="hidden" id="userName" name="userName" value="'+str(userName)+'">')
			print('<input type="hidden" id="password" name="password" value="'+str(password)+'">')
			print('<input type="hidden" id="employee" name="employee" value="False">')
			print('</br> </br>')
			print('<input class= "submit" id= "form_button" type="submit" style="float:right;" value="Update Contact Information">')
			print('</form>')
			print('</br> </br>')
			synAttacks = synFlood(results[0][0])
			
			print('<table class="tableCustomer" >')
			print('<tr>')
			print('<th>Attack type</th>')
			print('<th>Info</th>')
			print('<th>Attacks</th>')
			print('<th>Date-Time</th>')
			print('</tr>')
			for synAttack in synAttacks:
				portCounts = synAttacks[synAttack]
				for portCount in portCounts:
					print('</tr>')
					print('<td>Packet Flood</td>')
					print('<td>Packet Flag: [SYN]</td>')
					print('<td>Port: '+str(portCount)+ ' Attacks: '+str(portCounts[portCount])+'</td>')
					print('<td>'+str(synAttack)+'</td>')
					print('</tr>')
			print('</table>')	
			

else:
	print('<h2 class="heading">&bull;Authentication Failed&bull;</h2>')
	print('<p class="description login">Click <a href="http://www.cybersecsoho.com/login.html">here</a> to retry.</p>')	

with open('/var/www/cybersecsoho.com/page_end.html', 'r') as end:
	content = end.readlines()

for i in content:
	print(i.rstrip('\n'))
	
cursor.close()
db.close()


