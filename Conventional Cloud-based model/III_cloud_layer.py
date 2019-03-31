# first of all import the socket library 
import socket	
import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
		 
#s1 is always the socket used to receive information from the previous layer process
#s2 is always the socket used to send information to the next layer process
# next create a socket object 
#Cloud computing layer receives the data from CDMFC Layer. So only s1 socket is needed.
s1 = socket.socket()		 
print "Receiving Socket for cloud computing layer is successfully created"

# reserve a port on your computer in our 
# case it is 12345 but it can be anything ; port no of cloud computing layer socket
port = 12350				
timestamps=[]
datano=[]
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s1.bind(('', port))	
print	 
print "Cloud computing layer socket binded to %s" %(port) 
print
# put the socket into listening mode 
s1.listen(5)	 
print "Cloud computing layer socket is listening"			

keyword_list=["killed","damaging","dense"]
# a forever loop until we interrupt it or 
# an error occurs 
print
c, addr = s1.accept()	 
print 'Got connection from', addr , " : CDMFC layer socket"
print
count=0
while True: 

# Establish connection with client. 
	
# send a thank you message to the client. 
	print "Message received from cloud sourcing layer",
	mssg=c.recv(1024)
	count=count+1
	if mssg=="":
		break 
	print mssg
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
		timestamps.extend([datetime.datetime.now()])
		datano.extend([count])
        c.send("Next message please!!!")
# Close the connection with the client 
plt.title('Conventional Cloud Based model')
plt.plot(timestamps,datano,linewidth=2.0)
plt.xlabel('Timestamps')
plt.ylabel('Datano')
plt.gcf().autofmt_xdate()
plt.show()
	

