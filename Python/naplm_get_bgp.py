import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.10.20.119', 'cisco', 'cisco123')
iosvl2.open()

ios_output = iosvl2.get_bgp_neighbors()
print(json.dumps(ios_output, sort_keys=True, indent=4))


iosvl2.close()
