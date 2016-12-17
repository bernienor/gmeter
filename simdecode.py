#!/usr/bin/python3

import struct






class simdecode:
  def __init__ (self, prot):
    self.protocoll = prot
    self.pardict.clear()
    # Raise exeption for undefined protocoll

    
def unpack(self,d)
  if(self.protocoll == "condor"):
    return(unpack_condor(d))
  if(self.protocoll == "Silent wings bin"):
    return(unpack_swb(l))
  # Raise exeption for undefined protocoll
  return(0.0)

def unpack_condor(self,d):
  parlist = l.split()
  self.pardict.clear()
  for param in parlist:
    mypar = param.decode("utf-8").split('=')
    mydict.append(mypar[0],mypar[1])
  return mylist #encoding ok? 
  
    
def unpack_swb(self, data):
  lookupnames = { 'timestamp', 'position_latitude', 'position_longitude',  'altitude_msl',
                  'altitude_ground', 'altitude_ground_45_inop', 'altitude_ground_forward_inop', 
                  'pitch', 'yaw', 'd_roll', 'd_pitch', 'd_yaw', 'vx', 'vy',  'vz', 
                  'vx_wind', 'vy_wind', 'vz_wind',  'v_eas', 'ax', 'ay', 'az', 
                  'angle_of_attack', 'angle_sideslip', ' vario', 'heading', 
                  'rate_of_turn', 'airpressure', 'density', 'temperature' }
    
  data = struct.unpack('Iddfffffffffffffffffffffffffff',data)
  return(zip(lookupnames,data)
    

