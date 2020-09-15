import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.10.20.113', 'cisco', 'cisco123')
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
print(json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosvl2.get_arp_table()
print(json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosvl2.ping('google.com')
print(json.dumps(ios_output, sort_keys=True, indent=4))

iosvl2.close()
