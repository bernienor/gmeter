# Simple analog meter driver fot Raspberry Pi using two IO-pins in PWM mode
#
# usage: 
#
# gm = meter(2,3) # initate new meter using pin 2 as positive and pin 3 as negative terminal (BCM numbering)
# gm.set(3) # set the meter output to 3.
#
#

import RPi.GPIO as IO


class meter:

    def __init__ (self, pinP, pinN):
#        print 'Meter init with pin', pinP, 'as positive and pin' , pinN, 'as negative'
        self.gain=9 # default, works on my setup
        self.offset=0
        IO.setwarnings(False)
        IO.setmode(IO.BCM)
        IO.setup(pinP,IO.OUT)
        IO.setup(pinN,IO.OUT)
        self.p=IO.PWM(pinP,100)
        self.n=IO.PWM(pinN,100)
        self.p.start(50)
        self.n.start(50)
        self.set(0)
        
    def set(self, value):
            x=self.limit(-50,50,(self.gain * (self.offset + value)))
            self.p.ChangeDutyCycle(50+x)
            self.n.ChangeDutyCycle(50-x)
            
    def set_gain(self,gain):
        self.gain=gain
        
    def set_offset(self,offset):
        self.offset=offset
        
    def limit(self,lower,upper,x):
        if(lower>upper):
            ul=lower
            ll=upper
        else:
            ul=upper
            ll=lower
        
        if(x<lower):
            return lower
        if(x>upper):
            return upper
        return x
                


def main():
    import sys, string
    import time

    time.sleep(1)
    gm = meter(14,15)
    fortegn = 1
    if(sys.argv[1:]):
        i = string.atoi(sys.argv[1])
        if(i < 0) :
            i = 0 - i
            fortegn = -1   
        for x in range(i+1) :
            gm.set(x*fortegn)
            time.sleep(1)
    time.sleep(1)
  

if(__name__ == '__main__'):
    main()
