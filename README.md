# gmeter
Simple system for using analog meters as flight simulator instruments on a Raspberry Pi. Python code


The file gmaaler.py get UDP data from the flight simulator (in this case Condor).
The gmaaler sets up one instance of a gmeter and updates it with data from the simulator.


When hooking up a simple old analog elctrical variometer instrumen (like
from an old VP4, Bulsac or similar) put a 4k7 resistor in series with the
wires. One wire to pin 2 and the oter to pin 3 (BCM pin numbering).

The output is a bit jumpy. The PWM part of GPIO is not good enough for this
purpose. A better solution would be to output the data to a DAC to drive the
meter. An Arduino could easily do this job well.


A note on the difference between the condor protocoll on Condor and on Silent
Wings: Condor transmits one datagram for a complete dataset on the UDP port.
Whereas Silent Wings transmits one datagram for each parameter in the dataset.
This can give performance challenges if your not aware. 

In the flight simulator set the IP address to the address of the RPi.
