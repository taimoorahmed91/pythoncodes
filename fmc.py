import json
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/auth/generatetoken"
headers = {'Content-Type': 'application/json'}
user = 'taimoorahm'
pw = 'EBTKgKXJ'


# not using the .json() in the post method because it will return an empty response of 204
login_response = requests.post(url, auth=(user, pw), verify=False)
# print(login_response)

# Parse out the headers
resp_headers = login_response.headers
# print(resp_headers)
# Grab the token from the response headers
token = resp_headers.get('X-auth-access-token', default=None)


# Set the token in the headers to be used in the next call
headers['X-auth-access-token'] = token
# print(token)


url2 = 'https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/applications'
apps_response = requests.get(url2, headers=headers, verify=False).json()
# print(apps_response)

print(json.dumps(apps_response, indent=2, sort_keys=True))
