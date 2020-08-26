import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
switchuser = "devnetuser"
switchpassword = "Cisco123!"


myheaders = {"content-type": "application/json"}


response = requests.post(
    url,
    headers=myheaders,
    auth=(switchuser, switchpassword),
    verify=False,
).json()


token = response['Token']
# print(token)


url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/client-health"

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

scores = response_clients['response'][0]['scoreDetail']


for score in scores:
    if score['scoreCategory']['value'] == 'WIRED':
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
    elif score['scoreCategory']['value'] == 'WIRELESS':
        print(f"Wireless Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
