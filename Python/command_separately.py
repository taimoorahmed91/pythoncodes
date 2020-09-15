from netmiko import ConnectHandler

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.20.111',
    'username': 'cisco',
    'password': 'cisco123',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.20.112',
    'username': 'cisco',
    'password': 'cisco123',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.20.113',
    'username': 'cisco',
    'password': 'cisco123',
}

with open('commands') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
