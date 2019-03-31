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
#				cdmfc_X.extend([datetime.datetime.strptime(timestamps[0],"%H:%M:%S.%f")])
#			else:
#				conv_X.extend([datetime.datetime.strptime(line.rstrip(),"%H:%M:%S.%f")])	
#			Y.extend([cnt])
with open ("Analysis_Log.txt", "r") as fp:
    data=fp.readlines()		

count=0
for x in data:
	count=count+1
	timestamps=x.rsplit()
	cdmfc_X.extend([datetime.datetime.strptime(timestamps[0],"%H:%M:%S.%f")])	
	conv_X.extend([datetime.datetime.strptime(timestamps[1],"%H:%M:%S.%f")])
	Y.extend([count])	

#cdmfc_X=np.array(cdmfc_X)
#conv_X=np.array(conv_X)
#Y=np.array(Y)
linePlot.gcf().autofmt_xdate()
linePlot.plot(Y,cdmfc_X,color='red',label="CDMFC stats", marker='o')
linePlot.plot(Y,conv_X,color='blue',label="Conventional stats", marker='o')
linePlot.legend()
linePlot.xticks(range(1,count))
axes = linePlot.gca()

axes.set_ylim([datetime.datetime.strptime("0:00:00.020000","%H:%M:%S.%f"),datetime.datetime.strptime("0:00:00.070000","%H:%M:%S.%f")])
linePlot.xlabel("epoch no")
linePlot.ylabel("Time taken")

linePlot.title("Comparison of execution time periods between CDMFC model and conventional Cloud-based model")
linePlot.show()
