import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.10.20.119', 'cisco', 'cisco123')
iosvl2.open()

print('Accessing 10.10.20.119')
iosvl2.load_merge_candidate(filename='acl.cfg')
iosvl2.commit_config()
iosvl2.close()
