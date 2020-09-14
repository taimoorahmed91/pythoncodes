import json
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fmcrestapisandbox.cisco.com"
login_url = '/api/fmc_platform/v1/auth/generatetoken'
headers = {'Content-Type': 'application/json'}
user = 'taimoorahm'
pw = 'MdDxkEFE'


login_response = requests.post(
    f'{url}{login_url}', auth=(user, pw), verify=False)
# Parse out the headers
resp_headers = login_response.headers
# Grab the token from the response headers
token = resp_headers.get('X-auth-access-token', default=None)
print(token)


headers['X-auth-access-token'] = token

rules_url = '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/05056BB-0B24-0ed3-0000-893353384977/accessrules'

rules_payload = {
    "sendEventsToFMC": True,
    "action": "ALLOW",
    "enabled": True,
    "type": "AccessRule",
    "name": "Rule with custom",
    "logFiles": True,
    "logBegin": False,
    "logEnd": False,
    "variableSet": {
            "name": "Default Set",
            "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
            "type": "VariableSet"
    },
    "sourceNetworks": {
        "objects": [{
            "type": "NetworkGroup",
            "name": "10.10.20.0_24",
            "id": "005056BB-0B24-0ed3-0000-893353347143"
        }]
    },
    "destinationNetworks": {
        "objects": [{
            "type": "NetworkGroup",
            "name": "10.10.210.0_24",
            "id": "005056BB-0B24-0ed3-0000-893353272647"
        }]
    },
    "sourceZones": {
        "objects": [{
            "type": "SecurityZone",
            "name": "outside1",
            "id": "ac270386-648a-11e9-b96c-a85acdfd12d7"
        }]
    },
    "destinationZones": {
        "objects": [{
            "type": "SecurityZone",
            "name": "outside2",
            "id": "39d32f04-648e-11e9-b96c-a85acdfd12d7"
        }]
    },
    "filePolicy": {
        "name": "New Malware",
        "id": "59433a1e-f492-11e6-98fd-84ec1dfeed47",
        "type": "FilePolicy"
    }
}

rules_response = requests.post(f'{url}{rules_url}', headers=headers, data=json.dumps(
    rules_payload), verify=False).json()
print(' ******* RULES CREATED *******')
print(json.dumps(rules_response, indent=2, sort_keys=True))
print(' ******* RULES CREATED *******')
