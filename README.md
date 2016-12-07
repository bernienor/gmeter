# gmeter
Simple system for using analog meters as flight simulator instruments on a Raspberry Pi. Python code


The file gmaaler.py get UDP data from the flight simulator (in this case Condor).
The gmaaler sets up one instance of a gmeter and updates it with data from the simulator.


When hookin up a simple old analog elctrical variometer instrumen (like
from an old VP4, Bulsac or similar) put a 4k7 resistor in series with the
wires. One wire to pin 2 and the oter to pin 3 (BCM pin numbering).

In the flight simulator set the IP address to the address of the RPi.
