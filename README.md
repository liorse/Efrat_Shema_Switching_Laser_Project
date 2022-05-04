Problem description:
switching between two laser types from micromanager

Solution:
1. run NIS_ELEMENTs and micromanager
2. activate the relevant environment 
3. run a python server.py

4. micromanager sends a get command to 127.0.0.1:80 port e.g.
127.0.0.1:80/change_to_Laser_1
or for 
127.0.0.1:80/change_to_Laser_2

5. the server recieves the get command and send the appropriate keyboard shortcut which in turn runs a prewritten script in NIS-ELEMENTS