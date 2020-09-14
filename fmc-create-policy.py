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


# Authentication part is done till here

pol_url = '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies'


payload = {
    "type": "AccessPolicy",
    "name": "Taimoor Policy via API",
    "description": "Demo policy by Taimoor",
    "defaultAction": {
        "intrusionPolicy": {
            "name": "Security Over Connectivity",
            "id": "abba9b63-bb10-4729-b901-2e2aa0f4491c",
            "type": "IntrusionPolicy"
        },
        "variableSet": {
            "name": "Default Set",
            "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
            "type": "VariableSet"
        },
        "type": "AccessPolicyDefaultAction",
        "logBegin": False,
        "logEnd": True,
        "sendEventsToFMC": True
    }
}


pol_response = requests.post(
    f'{url}{pol_url}', headers=headers, data=json.dumps(payload), verify=False).json()
print(' ******* POLICY CREATED *******')
print(json.dumps(pol_response, indent=2, sort_keys=True))
print(' ******* POLICY CREATED *******')
policyId = pol_response['id']

print(policyId)
