from bluetooth import *

dev_list = discover_devices()
for device in dev_list:
    name = str(lookup_name(device))
    print('[+] Found Bluetooth device: ' + str(name))
    print('[+] Mac Address: ' + str(device))
