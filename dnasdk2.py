from dnacentersdk import api
import json
import time
import calendar
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

dna = api.DNACenterAPI(base_url='https://dcloud-dna-center-inst-rtp.cisco.com',
                       username='demo', password='demo1234!', verify=False)

print(dna)

sites = dna.networks.get_site_topology()

print(sites)
