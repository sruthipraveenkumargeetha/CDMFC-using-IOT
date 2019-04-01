# first of all import the socket library 
import socket			 
#s1 is always the socket used to receive information from the previous layer process
#s2 is always the socket used to send information to the next layer process

#Crowd-sourcing layer receives sensing data from the sensing layer and sends the data to CDMFC layer

# next create a socket object 
s1 = socket.socket()		 
print "Socket for crowd-sourcing layer is successfully created"
print
# reserve a port on your computer in our 
# case it is 12345 but it can be anything. port no of the crowd-sourcing layer socket.
port = 12345				

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s1.bind(('127.0.0.1', port))		 
print "Crowd-sourcing layer socket binded to %s" %(port) 
print
# put the socket into listening mode 
s1.listen(5)	 
print "Crowd-sourcing layer socket is listening"
print			
mssg=""
# a forever loop until we interrupt it or 
# an error occurs 
keywords_list=["winds","arctic","wind","fog","lightning","temperature","temperatures","earthquake","earthquakes","landfall",
"landfalls","tornado","tornadoes",
"dead","hurricane","hurricanes","injury","injuries","damage","dead","major","gusts","deficit","rainfall","cold"]

# Establish connection with client. 
c, addr = s1.accept()	 
print 'Got connection from', addr ,": Sensing layer socket" 
# Create a socket object 
print "Socket to send data to CDMFC layer is created successfully"
print
s2 = socket.socket()		 

# Define the port on which you want to connect ; 12347 is the port no for the CDMFC layer socket.
port2 = 12347				

# connect to the socket of CDMFC layer socket
print "Crowd-sourcing layer is connected to the socket of the CDMFC Layer"
s2.connect(('127.0.0.1', port2)) 
ack=""
while True:
	mssg=c.recv(1024)
	if mssg=="":
		break
	print
	print "Message received from sensing layer", mssg
 
 	print


#sending part to CDMFC layer
        flag=0
	for x in keywords_list:
		if x in mssg:
			flag=1
	if flag==1:
		s2.send(mssg)
		print
		print "Data sent from Crowdsourcing layer to CDMFC layer" 
		ack= s2.recv(1024)#recv ack from cdmfc layer
		c.send(ack)
	else:
		c.send("Next data");
		
	
s2.close()	 

