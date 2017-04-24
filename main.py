import binascii
import pycom
import time
from network import Bluetooth

pycom.heartbeat(False)      # turn off LED

bluetooth = Bluetooth()
bluetooth.start_scan(20)

while bluetooth.isscanning():
    adv = bluetooth.get_adv()
    if adv != None:
        # try to get the complete name
        adv_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL)
        if adv_data != None:
            print(adv_data)

        mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)

        if mfg_data:
            # try to get the manufacturer data (Apple's iBeacon data is sent here)
            print(binascii.hexlify(mfg_data))
