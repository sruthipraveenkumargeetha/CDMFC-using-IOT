# first of all import the socket library 
import socket			 
#s1 is always the socket used to receive information from the previous layer process
#s2 is always the socket used to send information to the next layer process
# next create a socket object 
#Cloud computing layer receives the data from CDMFC Layer. So only s1 socket is needed.
s1 = socket.socket()		 
print "Receiving Socket for cloud computing layer is successfully created"

# reserve a port on your computer in our 
# case it is 12345 but it can be anything ; port no of cloud computing layer socket
port = 12350				

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

# a forever loop until we interrupt it or 
# an error occurs 
print
c, addr = s1.accept()	 
print 'Got connection from', addr , " : CDMFC layer socket"
print
while True: 

# Establish connection with client. 
	
# send a thank you message to the client. 
	print "Message received from CDMFC layer",
	mssg=c.recv(1024)
	if mssg=="":
		break 
	print mssg
        c.send("Next message please!!!")
# Close the connection with the client 
	

