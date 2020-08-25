import requests

url = "https://172.16.30.102/api/aaaLogin.json"

payload = "{\n    \"aaaUser\":{\n        \"attributes\":{\n            \"name\":\"cisco\",\n            \"pwd\":\"cisco\"\n        }\n    }\n}"
headers = {
    'Content-Type': 'application/json',

}

response = requests.post(url, headers=headers,
                         data=payload, verify=False).json()

# print(response)

token = response['imdata'][0]['aaaLogin']['attributes']['token']

print(token)

# in python you can not use token , you need to use it in the form of a cookie
cookies = {}
cookies['APIC-cookie'] = token


# from here is the change request


url = "https://172.16.30.102/api/node/mo/sys/intf/phys-[eth1/11].json"

payload = "{\n    \"l1PhysIf\":{\n        \"attributes\":{\n            \"descr\":\"updated via python\"\n        }\n    }\n}"
headers = {
    'Content-Type': 'application/json',


}

put_response = requests.put(
    url, headers=headers, data=payload, cookies=cookies, verify=False).json()

print(put_response)
