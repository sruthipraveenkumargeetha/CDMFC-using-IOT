import matplotlib.pyplot as linePlot
import glob
import datetime
import numpy as np
cdmfc_X=[]
conv_X=[]
Y=[]
#filepath = 'Analysis_Log.txt'  
#files=glob.glob(filepath)
#for name in files:
#	with open(name) as fp:  
#		for cnt, line in enumerate(fp):

#			if(cnt%2==0):
#				cdmfc_X.extend([datetime.datetime.strptime(line.rstrip(),"%H:%M:%S.%f")])
#			else:
#				conv_X.extend([datetime.datetime.strptime(line.rstrip(),"%H:%M:%S.%f")])	
#			Y.extend([cnt])
with open ("Analysis_Log.txt", "r") as fp:
    data=fp.readlines()		

count=0
for x in data:
	count=count+1
	timestamps=x.rsplit()
	cdmfc_X.extend([timestamps[0]])	
	conv_X.extend([timestamps[1]])
	Y.extend([count])	

#cdmfc_X=np.array(cdmfc_X)
#conv_X=np.array(conv_X)
#Y=np.array(Y)
linePlot.plot(cdmfc_X,Y,color='red',label="CDMFC stats")
linePlot.plot(conv_X,Y,color='blue',label="Conventional stats")
linePlot.legend()

linePlot.xlabel("epoch no")
linePlot.ylabel("Time taken")
linePlot.gcf().autofmt_xdate()
linePlot.title("Comparison of execution time periods between CDMFC model and conventional Cloud-based model")
linePlot.show()
