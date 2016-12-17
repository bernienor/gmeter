#!/usr/bin/python3
import socket
import meter
import struct


def extract_g(l,protocoll):
  """
  >>> extract_g('gforce=1.2',"condor")
  1.2
  >>> extract_g('anotervar=12',"condor")
  
  """
  if(protocoll == "condor"):
    return(unpack_condor(l))
  if(protocoll == "Silent wings bin"):
    return(unpack_swb(l))
  return(0.0)

def unpack_condor(l):
  parlist = l.split()
  for param in parlist:
    mypar = param.decode("utf-8")
    mypar = mypar.split('=')
    if('gforce' == mypar[0]):
      return mypar[1]
  return 0.0
  
def update_g(param, value):
  if('gforce' == param): 
      print(value)

def unpack_swb(data):
  newdata = struct.unpack('Iddfffffffffffffffffffffffffff',data)
  print((1-newdata[20]/9.81), (1-newdata[21]/9.81), (1-newdata[22]/9.81), "\n") 
  return(1-newdata[21]/9.81)

def main(argc,argv):
 
  UDP_IP = "192.168.0.100"
  #UDP_PORT = 5005
  UDP_PORT = 55278

  gm = meter.meter(14,15)
  vario=meter.meter(2,3)

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
  sock.bind((UDP_IP, UDP_PORT))

  protocoll = "condor"
  verbose = false
  decodeobj = simdecode('condor')


  while True:
##    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
##    if(protocoll == "condor"):
##      gm.set(float(extract_g(data, "condor")))
##    if(protocoll == "swbin"):
##      gm.set(float(extract_g(data, "Silent wings bin")))
##    if(protocoll == "swcondor"):
##      gm.set(float(extract_var(data, "Silent wings condor")))
##    if(verbose):
##      print(data)

class simdecode:
  def __init__ (self, type):
    if(type=="condor"):
      parameters = {'gforce'}
    else
      raise 'Simulator data format not supported'

