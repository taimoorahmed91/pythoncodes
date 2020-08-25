import requests

url = "https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet2/description"

payload = {}
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='

}

response = requests.request(
    "GET", url, headers=headers, data=payload, verify=False)

print(response.text.encode('utf8'))
