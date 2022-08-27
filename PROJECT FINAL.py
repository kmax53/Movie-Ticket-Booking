#!/usr/bin/env python
# coding: utf-8

# In[1]:


#DATABASE CREATION
import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE THEATRE")

#FIRSTCLASS
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="THEATRE")
mycursor=mydb.cursor()
mycursor.execute("Create Table Firstclass(Movie char(30), Availabletickets int, Cost int,Showtime TIME,Language varchar(10))")
sql = "INSERT INTO Firstclass (Movie, Availabletickets, Cost, Showtime, Language) VALUES (%s,%s,%s,%s,%s)"
val = [
    ("MASTER","64","200","09:00:00/12:00:00/15:30:00/18:00:00/21:30:00","Tam/Tel/Kan"),
    ("SooraraiPotru","88","200","12:00:00/15:30:00/18:00:00/21:30:00","Tam/Tel"),
    ("TENET","45","200","15:30:00/18:00:00","Eng/Tam"),
    ("Avatar-II","97","200","10:00:00/12:00:00/15:30:00/18:00:00","English"),
    ("RRR","75","200","08:00:00/12:00:00/15:30:00/18:00:00/21:30:00","Telugu")
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) inserted.")

#BALCONY
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="THEATRE")
mycursor=mydb.cursor()
mycursor.execute("Create Table Balcony(Movie char(30), Availabletickets int, Cost int,Showtime TIME,Language varchar(10))")
sql = "INSERT INTO Balcony (Movie, Availabletickets, Cost, Showtime, Language) VALUES (%s,%s,%s,%s,%s)"
val = [
    ("MASTER","14","270","18:00:00/21:30:00","Tam/Tel/Kan"),
    ("SooraraiPotru","23","270","15:30:00/18:00:00/21:30:00","Tam/Tel"),
    ("TENET","17","270","15:30:00/18:00:00","Eng/Tam"),
    ("Avatar-II","11","270","10:00:00/12:00:00","English"),
    ("RRR","25","270","15:30:00/18:00:00","Telugu")
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) inserted.")

#BOX
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="THEATRE")
mycursor=mydb.cursor()
mycursor.execute("Create Table BOX(Movie char(30), Availabletickets int, Cost int,Showtime TIME,Language varchar(10))")
sql = "INSERT INTO BOX (Movie, Availabletickets, Cost, Showtime, Language) VALUES (%s,%s,%s,%s,%s)"
val = [
    ("MASTER","3","350","18:00:00/21:30:00","Tam/Tel/Kan"),
    ("SooraraiPotru","8","350","15:30:00/18:00:00/21:30:00","Tam/Tel"),
    ("TENET","12","350","15:30:00/18:00:00","Eng/Tam"),
    ("Avatar-II","2","350","10:00:00/12:00:00","English"),
    ("RRR","15","350","15:30:00/18:00:00","Telugu")
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) inserted.")

#SNACKS
import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",passwd="root",database="THEATRE")
mycursor=connection.cursor()
mycursor.execute("CREATE TABLE Snacks(Items varchar(30),Price int(20))")
sql="INSERT INTO Snacks(Items,Price) VALUES(%s,%s)"
val=[
    ("Soft Drinks","250"),
    ("Icecream","150"),
    ("Popcorn","100"),
    ("Chips","50"),
    ("Samosa","25")
]
mycursor.executemany(sql,val)
connection.commit()
print(mycursor.rowcount, "record(s) inserted.")

#TABLES
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="THEATRE")
mycursor=mydb.cursor() 
mycursor.execute("show tables")
for i in mycursor:
    print(i)
    
#GETTING INPUT FROM USER
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="THEATRE")
mycursor=mydb.cursor() 

print("+=+=+=+=+=+=+THEATRE ZONE+=+=+=+=+=+=+")
print("-_-_-_-_-_-_-_-!WELCOME TO THEATRE ZONE!-_-_-_-_-_-_-_-")
print("Available Options:")
print("SIR/MAM")
print("WE KINDLY REQUEST YOU TO MAKE YOUR CHOICE,NOTE:BOOKING COST VARIES ACCORDING TO YOUR PREFERRED CHOICE#MENTIONED BELOW")
print(":FOR BEST EXPERIENCE WE WOULD PREFER YOU BOX=1:")
print(":MODERATE VIEW+COMFORT WE WOULD LIKE TO PREFER YOU BALCONY=2:")
print(":NORMAL EXPERIENCE+COMFORT WE WOULD PREFER YOU FIRST CLASS=3:")
print("1,2,3")
option=int(input("Please enter ur option:"))
print(" ")

if option==1:
    mycursor.execute("select*from firstclass")
    records=mycursor.fetchall()
    for i in records:
        print("Movie=",i[0],)
        print("Available Tickets=",i[1],)
        print("Cost=",i[2],)
        print("Showtime=",i[3],)
        print("Language=",i[4],"\n")

elif option==2:
    mycursor.execute("select*from balcony")
    records=mycursor.fetchall()
    for i in records:
        print("Movie=",i[0],)
        print("Available Tickets=",i[1],)
        print("Cost=",i[2],)
        print("Showtime=",i[3],)
        print("language=",i[4],"\n")
elif option==3:
    mycursor.execute("select*from box")
    records=mycursor.fetchall()
    for i in records:
        print("Movie=",i[0],)
        print("Available Tickets=",i[1],)
        print("Cost=",i[2],)
        print("Showtime=",i[3],)
        print("language=",i[4],"\n")

MOVIE=input("MOVIE NAME FROM THE ABOVE SCREENING MOVIES:")
TICKETS=int(input("NO OF TICKESTS:"))
CUSTOMERNAME=input("PLEASE ENTER YOUR NAME:") 
DATE=input('DD/MM/YYYY:')
SUMMARY_DETAILS_VIA=int(input("PLEASE ENTER YOUR MAIL ID OR MOBILE NO:"))
LANGUAGE=input("PLEASE ENTER YOUR PREFERRED LANGUAGE:")
import random
import time
print("*************Please wait!!!Your bill is being processed*************")
time.sleep(5)
if option==1:
    bill=TICKETS*200
elif option==2:
    bill=TICKETS*270
elif option==3:
    bill=TICKETS*350
seats=random.randrange(1,100)
print("Your seat numbers are::",seats,"-",seats+TICKETS)
print("Total amount==Rs ",bill)
time.sleep(3)
print("------------------Congratulations!!!-----------\\\\-Your tickets have been booked for", MOVIE,"on",DATE)
print("A message would be sent to your mobile number",SUMMARY_DETAILS_VIA,"Please show it at the ticket booth in front of the theatre")
print("Enjoy your show!!!!!!")
print("Snacks will be displayed below")

import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",passwd="root",database="THEATRE")
mycursor=connection.cursor()
mycursor.execute("SELECT* FROM Snacks")
records=mycursor.fetchall()
for i in records:
    print("Items:",i[0],)
    print("Price:",i[1],"\n")
import time
import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",passwd="root",database="THEATRE")
mycursor=connection.cursor()
print("*****WELCOME TO OUR CAFETERIA*****")
list1=[]
num=int(input("Number of Snacks that you are going to buy from our Cafeteria: "))
for i in range(1, num+1):
    x=input("Enter the snacks that you want from our Cafeteria: ")
    list1.append(x)
print("Snacks that you entered are:",list1)
time.sleep(3)
bill=0
for i in list1:
    mycursor.execute("SELECT*FROM Snacks")
    records=mycursor.fetchall()
    for j in records:
        if i==j[0]:
            print(j[0],"is available in our Cafeteria")
            bill=bill+j[1]
           
print("***Please wait your bill is on process***")
time.sleep(5)        
print("Your bill is: Rs.",bill)
print("Please collect your snacks at the theatre cafeteria before your show")
print("********************************THANK YOU VISIT AGAIN**********************************************")


# In[ ]:




