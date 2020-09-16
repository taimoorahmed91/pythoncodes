from netmiko import ConnectHandler
import sys
from datetime import datetime

with open('devices_file') as f:
    devices_list = f.read().splitlines()


for devices in devices_list:
    print('Connecting to device ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'cisco',
        'password': 'cisco123'
    }

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_command('term len 0')
    output1 = net_connect.send_command('show runn')

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    config_filename = 'config-' + devices + timestampStr
    file = open(config_filename, "w")
    file.write(output1)
    file.close()
