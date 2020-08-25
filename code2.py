from ncclient import manager
# import logging
# logging.basicConfig(level=logging.DEBUG)

router = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "10000",
          "username": "developer", "password": "C1sco12345"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for taimoor in m.server_capabilities:
        print('=*' * 50)
        print(taimoor)
    m.close_session()
