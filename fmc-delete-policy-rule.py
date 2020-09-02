import json
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fmcrestapisandbox.cisco.com"
login_url = '/api/fmc_platform/v1/auth/generatetoken'
headers = {'Content-Type': 'application/json'}
user = 'taimoorahm'
pw = 'h2Mcqwpc'


login_response = requests.post(
    f'{url}{login_url}', auth=(user, pw), verify=False)
# Parse out the headers
resp_headers = login_response.headers
# Grab the token from the response headers
token = resp_headers.get('X-auth-access-token', default=None)
print(token)


rule_url = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/005056BB-0B24-0ed3-0000-893353377696/accessrules/005056BB-0B24-0ed3-0000-000268490126"
headers['X-auth-access-token'] = token


del_response = requests.delete(
    f'{url}{rule_url}', headers=headers,  verify=False).json()
# print(json.dumps(del_response, indent=2, sort_keys=True))
