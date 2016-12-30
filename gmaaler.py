#!/usr/bin/python3
import socket
import meter
import sys
import simdecode as sim




def main():
 
  UDP_IP = "192.168.0.100"
  UDP_PORT = 55278

  gm = meter.meter(17,18)
#  vario=meter.meter(2,3)

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
  sock.bind((UDP_IP, UDP_PORT))

  protocoll = "condor"
#  protocoll = 'sw_condor'
#  protocoll = 'sw_bin'
  decode = sim.simdecode(protocoll)

  while True:
    i=0
    while(i<29): # Needed to speed up things when using condor protocoll on Silent Wings.
      data, addr = sock.recvfrom(4096)
      decode.unpack(data)
      i+=1
    gm.set(float(decode.get('gforce')))
#    vario.set(parameters.get('vario'))
    
if(__name__ == '__main__'):
    main()
