from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.10.20.113', 'cisco', 'cisco123')
iosvl2.open()

ios_output = iosvl2.get_facts()
print(ios_output)
