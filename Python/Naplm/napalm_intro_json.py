import json
from napalm import get_network_driver


driver = get_network_driver('ios')
iosvl2 = driver('10.10.20.113', 'cisco', 'cisco123')
iosvl2.open()

ios_output = iosvl2.get_facts()
print(json.dumps(ios_output, indent=4))


# you can find these via looking for support matrixx of naplm
# ios_output = iosvl2.get_interfaces()
# print(json.dumps(ios_output, sort_keys=True, indent=4))

# ios_output = iosvl2.get_interfaces_counters()
# print(json.dumps(ios_output, sort_keys=True, indent=4))

iosvl2.close()
