# first of all import the socket library 
import socket	
import datetime

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#s1 is always the socket used to receive information from the previous layer process
#s2 is always the socket used to send information to the next layer process

#CDMFC layer receives crowdsourced data from the crowdsourcing layer and sends the data to Cloud computing layer
# next create a socket object 
s1 = socket.socket()		 
print "Socket for CDMFC layer is successfully created"
print
# reserve a port on your computer in our 
# case it is 12345 ; port no of CDMFC layer socket
port = 12347				

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s1.bind(('', port))		 
print "CDMFC layer socket binded to %s" %(port) 
print
# put the socket into listening mode 
s1.listen(5)	 
print "CDMFC layer socket is listening"			

# a forever loop until we interrupt it or 
# an error occurs 
print
print "CDMFC socket to send data to cloud computing layer is created successfully"

#sending part to CDMFC layer
# Create a socket object 
s2 = socket.socket()		 

# Define the port ; port no of cloud computing layer
port2 = 12350				
print
# connect to the socket of cloud computing layer
s2.connect(('127.0.0.1', port2)) 

keyword_list=["killed","damaging","dense","damage","damages","dead","tornado","earthquake","intense","major","hurricane"]
timestamps=[]
datano=[]
# Establish connection with client. 
c, addr = s1.accept()
ack=""	 
print 'Got connection from', addr ," : Crowdsourcing layer socket"
print
count=0
# send a thank you message to the client. 
a=datetime.datetime.now()
while True:
	mssg=c.recv(1024)
	if mssg=="":
		break
	count=count+1
	print "Message received from Crowdsourcing layer", mssg
        
	print
	flag=0
	for x in keyword_list:
		if x in mssg:
			flag=1
			break
	if flag==1:
		print "***************************************************"
		print
		with open('Notifications.txt','ab') as f:
			f.write(str(datetime.datetime.now())+" --> "+mssg)
		timestamps.extend([datetime.datetime.now()-a])
		datano.extend([count])
		
	print "Date sent to Cloud computing layer"
	s2.send(mssg)
	ack=s2.recv(1024)
	c.send(ack)
plt.title('CDMFC model')
plt.plot(timestamps,datano,linewidth=2.0, marker='o', color='b')
plt.xlabel('Timestamps')
plt.ylabel('Datano')
plt.gcf().autofmt_xdate()
plt.show()
# close the connection 
s2.close()
