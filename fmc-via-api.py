import urllib3
import requests
import sys
import json
import mysql.connector

connection = mysql.connector.connect(host='130.211.216.63',
                                     database='firepower',
                                     user='root',
                                     password='taimoor1991')
sql_select_Query = "select * from access"
# MySQLCursorDict creates a cursor that returns rows as dictionaries
cursor = connection.cursor(dictionary=True)
cursor.execute(sql_select_Query)
records = cursor.fetchall()
for row in records:
    id = row["id"]
    name = row["name"]
    srczone = row["src-zone"]
    srczoneid = row["src_zone_id"]
    dstzone = row["dst_zone"]
    dstzoneid = row["dst_zone_id"]
    srcnetwork = row["src_network"]
    srcnetworkid = row["src_network_id"]
    dstnetwork = row["dst_network"]
    dstnetworkid = row["dst_network_id"]


print(id, name)


# your API here


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
    "name": name,
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
            "name": srcnetwork,
            "id": srcnetworkid
        }]
    },
    "destinationNetworks": {
        "objects": [{
            "type": "NetworkGroup",
            "name": dstnetwork,
            "id": dstnetworkid
        }]
    },
    "sourceZones": {
        "objects": [{
            "type": "SecurityZone",
            "name": srczone,
            "id": srczoneid
        }]
    },
    "destinationZones": {
        "objects": [{
            "type": "SecurityZone",
            "name": dstzone,
            "id": dstzoneid
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
