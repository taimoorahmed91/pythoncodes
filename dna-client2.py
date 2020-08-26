import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://dcloud-dna-center-inst-rtp.cisco.com/dna/system/api/v1/auth/token"
switchuser = "demo"
switchpassword = "demo1234!"


myheaders = {"content-type": "application/json"}


response = requests.post(
    url,
    headers=myheaders,
    auth=(switchuser, switchpassword),
    verify=False,
).json()


token = response['Token']
print(token)


url = "https://dcloud-dna-center-inst-rtp.cisco.com/dna/system/api/v1/auth/token"

querystring = {"timestamp": ""}

headers = {
    'x-auth-token': token,
    'Content-Type': 'application/json'
}

response_clients = requests.get(
    url, headers=headers, params=querystring, verify=False).json()

# print(response_clients)


print(
    f"Clients: {response_clients['response'][0]['scoreDetail'][0]['clientCount']}")
