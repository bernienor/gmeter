#!/usr/bin/python3

import struct


class simdecode:
  def __init__ (self, prot):
    self.protocoll = prot
    self.pardict = {}
    self.lookupnames = ('none')
    # Raise exeption for undefined protocoll

  def unpack(self, d):
    if(self.protocoll == 'condor'):
      parlist = d.decode("utf-8").split()
      for param in parlist:
        mypar = param.split('=')
        self.pardict[mypar[0]] = mypar[1]
    elif(self.protocoll == 'sw_condor'):
       pass
    elif(self.protocoll == 'sw_bin'):
       pass
    else:
       raise NameError('Unknown protocoll')
      
  def get(self, parameter):
    return self.pardict.get(parameter, 0)


    
"""    
Unfinished stuff for Silent Wings binary format. 
  def unpack_swb(self, data):
    self.lookupnames = ( 'timestamp', 'position_latitude', 'position_longitude',  'altitude_msl',
                    'altitude_ground', 'altitude_ground_45_inop', 'altitude_ground_forward_inop', 
                    'pitch', 'yaw', 'd_roll', 'd_pitch', 'd_yaw', 'vx', 'vy',  'vz', 
                    'vx_wind', 'vy_wind', 'vz_wind',  'v_eas', 'ax', 'ay', 'az', 
                    'angle_of_attack', 'angle_sideslip', 'vario', 'heading', 
                    'rate_of_turn', 'airpressure', 'density', 'temperature' )
      
    self.data = struct.unpack('Iddfffffffffffffffffffffffffff',data)
    #self.pardict = zip(lookupnames,data)
    for name, value in lookupnames, data
      self.pardict.add(name,value)
      


  def get_variable(self, var):
    return self.pardict.get(var)
 

"""

    


           


