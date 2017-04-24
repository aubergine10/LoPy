import pycom
import time
pycom.heartbeat(False)
for cycles in range(10): # stop after 10 cycles
    #pycom.rgbled(0x007f00) # green
    pycom.rgbled(0x000300) # green
    time.sleep(5)
    #pycom.rgbled(0x7f7f00) # yellow
    pycom.rgbled(0x030300) # yellow
    time.sleep(1.5)
    #pycom.rgbled(0x7f0000) # red
    pycom.rgbled(0x030000) # red
    time.sleep(4)
