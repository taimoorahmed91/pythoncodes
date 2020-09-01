from dnacentersdk import api
import json
import time
import calendar
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com',
                       username='devnetuser', password='Cisco123!', verify=False)


# print(dna)


# # Print all the sites only
# sites = dna.topology.get_site_topology()
# for site in sites.response.sites:
#     print(site)
#     print(site.groupNameHierarchy)
#     print(site.id)
#     print(" ")

#     print(json.dumps(site, indent=2, sort_keys=True))

# ############### DEVICES #############
# devices = dna.devices.get_device_list()
# print(devices)
# print(json.dumps(devices, indent=2, sort_keys=True))
# for device in devices.response:
#     print(device)
#     print(device.id)

########################SPCIFIC DEVICE when it not an array##############################

# specific = dna.devices.get_device_by_id(
#     '1cfd383a-7265-47fb-96b3-f069191a0ed5')
# print(specific)

# print(json.dumps(specific, indent=2, sort_keys=True))
# print(
#     f"Your hostname is {specific['response']['hostname']}")

########################SPCIFIC DEVICE when it not an array##############################

# ipspecific = dna.devices.get_network_device_by_ip('10.10.22.73')
# print(ipspecific)

# print(json.dumps(ipspecific, indent=2, sort_keys=True))
# print(
#     f"Your hostname is {ipspecific['response']['hostname']}")


############# CLIENTS ##############
# Get Client Health with Epoch Datetime
# epoch_datetime = calendar.timegm(time.gmtime())

# client_health = dna.clients.get_overall_client_health()

# print(json.dumps(client_health, indent=2, sort_keys=True))
# print(' ')

site_health = dna.sites.get_site_health()
print(json.dumps(site_health, indent=2, sort_keys=True))
print(' ')
