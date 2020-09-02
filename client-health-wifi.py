import requests
import json

################ LOGIN ######################
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
pw = 'Cisco123!'

response = requests.post(url, auth=(user, pw), verify=False).json()
# print(response)
token = response['Token']

############ GET CLIENT DETAIL ################
macAddress = '00:1E:13:A5:B9:40'
url = f"https://sandboxdnac.cisco.com/dna/intent/api/v1/client-detail?timestamp=&macAddress={macAddress}"


headers = {
    'x-auth-token': token,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers, verify=False).json()

print(json.dumps(response, indent=2, sort_keys=True))
device_details = response['topology']['nodes']
print(device_details)

# for device_detail in device_details:
#     if device_detail['id'] == device_details[0]['id']:
#         print(f"Client IP: {device_detail['ip']}")
#         print(f"MAC: {device_detail['id']}")
#         print(f"Health Score: {device_detail['healthScore']}")
#         print(" ")
#     elif device_detail['id'] == device_details[1]['id']:
#         print(f"Connected to {device_detail['deviceType']}")
#         print(f"WAP IP: {device_detail['ip']}")
