import requests
import json
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://172.16.30.101/ins"
switchuser = "cisco"
switchpassword = "cisco"


myheaders = {"content-type": "application/json"}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show interface switchport",
        "output_format": "json",
    }
}
response = requests.post(
    url,
    data=json.dumps(payload),
    headers=myheaders,
    auth=(switchuser, switchpassword),
    verify=False,
).json()


# from here is the authentication part


auth_url = "https://172.16.30.101/api/mo/aaaLogin.json"

auth_body = {"aaaUser": {"attributes": {
    "name": switchuser, "pwd": switchpassword}}}


auth_response = requests.post(
    auth_url, json=auth_body, timeout=5, verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']

# print(token)


cookies = {}
cookies['APIC-cookie'] = token

# print(cookies)

# your logic starts here


max_interface = 28
counter = 0

while counter < max_interface:

    interface = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface'][counter]['interface']
    operation_mode = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface'][counter]['oper_mode']
    access_vlan = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface'][counter]['access_vlan']
    access_vlan_name = response['ins_api']['outputs']['output']['body'][
        'TABLE_interface']['ROW_interface'][counter]['access_vlan_name']
    counter += 1

    print(interface)

    body = {
        "l1PhysIf": {
            "attributes": {
                "descr": 'Interface '+interface+' mode '+operation_mode+' vlan name ' + access_vlan_name
            }
        }
    }
    if operation_mode != 'trunk':

        # FORMAT THE INTERFACE NAME TO BE LIKE ETH1/1 TO CONSTRUCT URL

        int_name = str.lower(str(interface[:3]))
        int_num = re.search(r'[1-9]/[0-9]*', interface)

        # print(int_name+str(int_num.group(0)))
        int_url = 'https://172.16.30.101/api/mo/sys/intf/phys-['+int_name+str(
            int_num.group(0))+'].json'

        post_response = requests.put(int_url, data=json.dumps(
            body), headers=myheaders, cookies=cookies, verify=False).json()
        print(post_response)
