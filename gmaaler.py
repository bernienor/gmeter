import socket
import meter



def extract_g(l):
  """
  >>> extract_g('gforce=1.2')
  1.2
  >>> extract_g('anotervar=12')
  
  """
  parlist = l.split()
  for param in parlist:
    mypar = param.decode("utf-8")
    mypar = mypar.split('=')
    if('gforce' == mypar[0]):
      return mypar[1]
  return 0

def update_g(param, value):
  if('gforce' == param): 
      print(value)

 
UDP_IP = "192.168.0.116"
#UDP_PORT = 5005
UDP_PORT = 55278

gm = meter.meter(2,3)

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


while True:
  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  gm.set(float(extract_g(data)))
  #print(data)


