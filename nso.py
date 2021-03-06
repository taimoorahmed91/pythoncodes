import requests
import json

# Dont forget sudo ufw allow 8080
url_base = 'https://10.10.20.49/api'
auth = ("developer", "C1sco12345")

# Other useful headers

#    'application/vnd.yang.api+json',
#    'application/vnd.yang.datastore+json',
#    'application/vnd.yang.data+json',


headers = {'Accept': 'application/vnd.yang.collection+json'}

# Get request to NSO
response = requests.get(
    f'{url_base}/running/devices/device', auth=auth, headers=headers, verify=False).json()
# print(json.dumps(response, indent=2, sort_keys=True))

# Parse out devices from response body
devices = response['collection']['tailf-ncs:device']
for device in devices:
    print(f"Name: {device['name']}")
    print(f"IP: {device['address']}")
    print(f"SSH Port: {device['port']}")
    print(f"Auth Group: {device['authgroup']}")
    # print(device)
    print(" ")
