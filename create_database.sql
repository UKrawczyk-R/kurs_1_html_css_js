/* create database*/

CREATE DATABASE CyberSec_SOHO;
 USE CyberSec_SOHO;

/* 1a-  customers  table*/
CREATE TABLE customers(
customer_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
first_name varchar(30),
last_name varchar(30),
company_name varchar(30),
address varchar(30),
city varchar(20),
state varchar(2),
zip_code varchar(5),
email varchar(30),
phone varchar(11)
);

/* 2a - customers records */
INSERT INTO customers VALUES 
(DEFAULT,'Jan','Nowak','Salt&Sweet','12 Mickiewicza st.','Rzeszow','PL','35333','j.n@salatsweet.com','48111222333'),
(DEFAULT,'Monika','Szalajko','Modentus','20a Padereskiego st.','Rzeszow','PL','35328','m.sz@.modentus.com','48222333444'),
(DEFAULT,'Joanna','Leniart','ForKidsFun','105 Armii Krajowej st.','Rzeszow','PL','35335','j.l@.forkidsfun.com','48333444555');



/* 3a - query customer info */
SHOW COLUMNS FROM customers;

SELECT *
FROM customers;


/* 1b-  employees  table*/
CREATE TABLE employees
(
employee_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
first_name varchar(30),
last_name varchar(30),
email varchar(30),
job_position varchar(30)
);

/* 2b - employees records */
INSERT INTO employees VALUES 
(DEFAULT,'Pat','Walt','p.w@cybersec_soho.com','network enginner'),
(DEFAULT,'Adam','Smith','a.s@cybersec_soho.com','support'),
(DEFAULT,'kat','First','k.w@cybersec_soho.com','programmer'),
(DEFAULT,'Mat','Last','m.l@cybersec_soho.com','data enginner');

/* 3b - query cemployees info */
SHOW COLUMNS FROM employees;

SELECT *
FROM employees;


/* 1c- login table*/
CREATE TABLE login
(
login_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
person_id int,
userName varchar(30),
passwd varchar(30),
type varchar(11)
);

/* 2c - login records */
INSERT INTO login VALUES 
(DEFAULT,1,'PWalt','password','employee'),
(DEFAULT,2,'ASmith','password','employee'),
(DEFAULT,3,'KFirst','password','employee'),
(DEFAULT,4,'MLast','password','employee'),
(DEFAULT,1,'JNowak','password','customer'),
(DEFAULT,2,'MSzalajko','password','customer'),
(DEFAULT,3,'JLeniart','password','customer');

/* 3c - query login info */
SHOW COLUMNS FROM login;

SELECT *
FROM login;

/* 1d- incidents table*/
CREATE TABLE incidents
(
incydent_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
packetDateTime datetime,
srcIP varchar(30),
destIP varchar(30),
protocol varchar(10),
srcPort varchar(6),
destPort varchar(6),
hostIP varchar(20),
serverIP varchar(20),
srcMac varchar(17),
destMac varchar(17),
info text,
customer_id int
);

/* 2d - incidents records */
INSERT INTO incidents VALUES 
(DEFAULT,'2023-02-08 03:20:00','172.16.137.40','172.16.137.40','DHCP','68','67','172.16.137.40','172.16.137.1','08:00:2b:ef:ab:7c','00:1d:7e:7c:c4:8d','DHCP Request  - Transaction ID 0xfe9ceb09',1),
(DEFAULT,'2023-03-08 13:20:15','172.16.137.1','172.16.137.1','DHCP','67','68','172.16.137.1','255.255.255.255','00:1d:7e:7c:c4:8d','ff:ff:ff:ff:ff:ff','DHCP ACK      - Transaction ID 0xfe9ceb09',1),
(DEFAULT,'2022-08-24 10:35:30','10.100.25.14','10.100.25.14','TCP','1065','139','10.100.25.14','10.100.18.12','00:15:c5:3c:4f:9e','00:03:ff:6c:8b:24','1065  >  139 [SYN] Seq=0 Win=8 Len=0',2),
(DEFAULT,'2022-09-24 10:35:15','10.100.25.14','10.100.25.14','TCP','19491','135','10.100.25.14','10.100.18.12','00:15:c5:3c:4f:9e','00:03:ff:6c:8b:24','19491  >  135 [SYN] Seq=0 Win=8 Len=0',2),
(DEFAULT,'2022-10-24 10:35:35','10.100.25.14','10.100.25.14','TCP','7358','445','10.100.25.14','10.100.18.12','00:15:c5:3c:4f:9e','00:03:ff:6c:8b:24','7358  >  445 [SYN] Seq=0 Win=8 Len=0',2),
(DEFAULT,'2022-07-10 11:32:42','23.67.253.43','23.67.253.43','TCP','80','49163','54.10.120.45','192.168.137.83','a8:b1:d4:ac:fe:7d','00:21:9b:5b:d1:7a','80  >  49163 [SYN, ACK] Seq=0 Ack=1 Win=14600 Len=0 MSS=1367 SACK_PERM=1 WS=32',3), 
(DEFAULT,'2022-08-10 11:32:55','192.168.137.83','192.168.137.83','TCP','49163','80','192.168.137.83','54.10.120.45','00:21:9b:5b:d1:7a','a8:b1:d4:ac:fe:7d','49163  >  80 [ACK] Seq=1 Ack=1 Win=65536 Len=0',3),
(DEFAULT,'2022-09-10 11:32:21','192.168.137.83','192.168.137.83','HTTP','49163','80','192.168.137.83','54.10.120.45','00:21:9b:5b:d1:7a','a8:b1:d4:ac:fe:7d','HEAD /v9/windowsupdate/redir/muv4wuredir.cab?1507101531 HTTP/1.1',3),
(DEFAULT,'2022-10-10 11:32:38','23.67.253.43','23.67.253.43','TCP','80','49163','54.10.120.45,192','168.137.83','a8:b1:d4:ac:fe:7d','00:21:9b:5b:d1:7a','80  >  49163 [ACK] Seq=1 Ack=174 Win=15680 Len=0',3);

/* 3d - query incidents info */
SHOW COLUMNS FROM incidents;

SELECT *
FROM incidents;

/* -queries */

/*3a- query 1*/

SELECT first_name, last_name, company_name, email, userName
FROM customers JOIN login
ON customers.customer_id = login.person_id
WHERE type ='customer';

/*3b -query 2*/

SELECT employee_id, first_name, last_name, email, job_position, userName
FROM employees JOIN login
ON employees.employee_id = login.person_id
WHERE type ='employee';

/*3c -query 3*/

SELECT first_name, last_name, company_name, srcIP, destIP, info
FROM customers JOIN incidents
USING(customer_id);

/* 3d query 4 */

SELECT concat_ws('\n', concat(first_name,' ', last_name), company_name, address, 
concat(city,' ', state,' ', zip_code)) AS mailingAddress
FROM customers;

/* 4e query 5 */
SELECT company_name, count(incydent_id)
FROM customers JOIN incidents
USING(customer_id)
GROUP BY company_name;


/* 4f query 6*/
USE CyberSec_SOHO;




SELECT customers.company_name, incydentCount
FROM customers INNER JOIN incidents USING(customer_id)
INNER JOIN
	(SELECT incydentCount
	FROM 
		(SELECT customer_id, count(incydent_id) AS incydentCount
		FROM incidents
		GROUP BY customer_id)
		AS info
	WHERE incydentCount IN
		(SELECT max(incydentCount)
		FROM
			(SELECT customer_id, count(incydent_id) AS incydentCount
			 FROM incidents
			 GROUP BY customer_id)
			 AS info
		UNION
		SELECT min(incydentCount)
		FROM
			(SELECT customer_id, count(incydent_id) AS incydentCount
			 FROM incidents
			 GROUP BY customer_id)
			 AS info))
	AS temp 
    ORDER BY incydentCount;

/* 4f query 7*/

SELECT customer_id,  date(packetDateTime) AS lastIncident,
datediff(curdate(), date(packetDateTime)) AS daysSinceLastIncident
FROM incidents
ORDER BY date(packetDateTime) desc;
    

	





