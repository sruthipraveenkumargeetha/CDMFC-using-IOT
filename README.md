# CDMFC-using-IOT

HOW TO RUN?

There are two different models implemented - the proposed CDMFC model and the conventional cloud-based model.
Download and unzip the project contents.

Running CDMFC model:
1. Change the current working directory into 'CDMFC model'
2. Run each of the III_cloud_layer.py, II_CDMFC_layer.py, I_crowdsourcing_layer.py, 1_sensing_layer.py 
in four different terminals.

After the execution of model, a graph is generated from CDMFC layer showing the datano vs timestamp. (Refer the documentation provided 
for detailed understanding). Notifications.txt file is also filled by the CDMFC layer.

To run the conventional cloud-based model, 
1. Change the current working directory into 'Conventional Cloud-based model'.
2. Run each of the III_cloud_layer.py, I_crowdsourcing_layer.py, 1_sensing_layer.py 
in three different terminals.

After the execution of model, a graph is generated from cloud layer showing the datano vs timestamp. (Refer the documentation provided 
for detailed understanding). Notifications.txt file is also filled by the cloud layer.

For generating the comparison graph, the key is to execute CDMFC model first and then conventional cloud-based model next.
Each sequential combined iteration will append a line of pair of timestamps in the Analysis_Log.txt. 

Run python generate_log.py to generate the comparison graph showing the variation between CDMFC model and the combined cloud-based model
vs iteration number. 
Visualization folder is provided in the directory of each model to store the generated graphs.

