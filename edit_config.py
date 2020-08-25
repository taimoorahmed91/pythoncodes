from ncclient import manager
from router_info import router

config_template = open(
    "/home/taimoor/PythonCodes/edit_conf.xml").read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="Devnet Class of 2020", ipaddress='2.2.2.3', subnetmask='255.255.255.0')

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)
