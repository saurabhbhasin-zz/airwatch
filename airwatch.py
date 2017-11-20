# Get devices from Airwatch

# To use this, you must fill out:
# 1. Your Airwatch tenant host
# 2. Your REST API Key
# 3. Username and Password for Basic Authentication

import requests
import logging
import csv

host = "https://YOURTENANT.awmdm.com"
endpoint = "/api/mdm/devices/search?pagesize=1000"
url = host + endpoint
key = "YOUR REST API KEY"
headers = {"aw-tenant-code": key, "Accept": "application/json", "Content-Type":
           "application/json"}

logging.basicConfig(filename='aw.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

r1 = requests.get(url, headers=headers, auth=('USERNAME', 'PASSWORD'))

if r1.status_code == 200:
    response = r1.json()
    devices = response['Devices']
    devicecount = 'Found %s devices' % len(devices)
    logging.info(devicecount)
    with open("airwatch_devices.csv", 'w') as target:
        writer = csv.writer(target, delimiter=",")
        writer.writerow(["User Name", "User Email", "Serial Number", "Model",
                        "Device Friendly Name", "Enrollment Status"])
        logging.info("====Getting Devices====")
        for i in devices:
            row = i["UserName"], i["UserEmailAddress"], i["SerialNumber"], i["Model"], i["DeviceFriendlyName"], i["EnrollmentStatus"]
            writer.writerow(row)
            logging.info(row)
    target.close()
else:
    print("Invalid REST API Response. See log for details")
    logging.info(r1.status_code)
