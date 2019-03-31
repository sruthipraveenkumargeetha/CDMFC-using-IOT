# Import socket module 
import socket	

import datetime
import glob
#s1 is always the socket used to receive information from the previous layer process
#s2 is always the socket used to send information to the next layer process

#Sensing layer only has to send info to Crowd sourcing layer. It does not have to receive the data from any previous layer. Therefore,only
#socket s2 is created
# Create a socket object 
s2 = socket.socket()		 
print "Socket for Sensing Layer is created successfully"
print
# Define the port on which you want to connect, here it is the port no of the receiving socket of Crowd sourcing layer
port = 12345				

# connect to the crowd sourcing layer, insert the ip of the machine in which crowdsourcing layer is running for this to work 
s2.connect(('127.0.0.1', port)) 
print "Sensing layer socket connected to Crowd-sourcing layer socket"
print 

a = datetime.datetime.now()
filepath = '../Sensor data/Sensor_0001.txt'  
files=glob.glob(filepath)
for name in files:
	with open(name) as fp:  
		for cnt, line in enumerate(fp):
			sensingdata=line
			print "Sensing data :", sensingdata 
			s2.send(sensingdata)
			print
			print "Sensing data sent to Crowd-sourcing layer" 
			print s2.recv(1024) #recv ack
	 
b = datetime.datetime.now()
print "Time taken",(b-a)
with open('../Analysis_Log.txt','ab') as f:
	f.write(str(b-a)+"\t")
