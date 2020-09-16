import json
from napalm import get_network_driver

devicelist = ['10.20.20.119',
              '10.20.20.120'
              ]

for ip_address in devicelist:
    print("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv = driver(ip_address, 'cisco', 'cisco123')
    iosv.open()
    iosv.load_merge_candidate(filename='acl.cfg')
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No ACL changes required.')
        iosv.discard_config()

    iosv.load_merge_candidate(filename='ospf1.cfg')

    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No OSPF changes required.')
        iosv.discard_config()

    iosv.close()
