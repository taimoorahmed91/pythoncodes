import json
from napalm import get_network_driver

bgplist = ['10.10.20.119',
           '10.10.20.120'
           ]
for ip_address in bgplist:
    print("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'cisco', 'cisco123')
    iosv_router.open()
    bgp_neighbors = iosv_router.get_bgp_neighbors()
    print(json.dumps(bgp_neighbors, indent=4))
    iosv_router.close()
