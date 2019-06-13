.. Example documentation

Examples
========

PyIGN Initialize System States
------------------------------

To initialize and run the software, a class instance of the system states is be created and output to command line. The initial state of the system should always be 'SAFE MODE'. Input the following into command line from the PyIGN folder, to verify the system initialized without error::

    python functions -s

The resulting output represents the Valves, Ignitor, GO/NOGO, ABORT, and Nanny states.

PyIGN Test Go/NoGo Detection
----------------------------

To test the automatic "GO/NOGO" sequence, a class instance of the system states is be created and output to command line. Next, both of the Control Panel and Fuel Panel "GO/NOGO" states are set to "GO", then output to command line. Next, the "Ignitor" state is turned "ACTIVE" but with the state is output to command line, "SAFE MODE" is returned due to the LOX Panel state being "GO/NOGO". Last, the LOX Panel "GO/NOGO" state is switched to "GO" and the "Ignitor" state is turned to "ACTIVE". Input the following into command line from the PyIGN folder, to verify the systems GO/NOGO detection::

    python functions -g

The resulting output represents the Ignitor, and GO/NOGO states.

PyIGN Test Abort Detection
--------------------------

To test the automatic "ABORT" sequence, a class instance of the system states is be created and valves are set to "ACTIVE" states and output to command line. Next, "NANNY MODE" is turned "ON" and enables the system to automatically trip an "ABORT" if sensed data exceeds set sensor limits. Simulated sensor data is then read in and compared to the initialized sensor limits. Last, the "ABORT" sequence is tripped, and the system switches all states to "SAFE MODE". Input the following into command line from the PyIGN folder, to verify the systems abort detection::

    python functions -t

The resulting output represents the Valves, ABORT, and Nanny states.
