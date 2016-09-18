'''
    File name: show_bus_locations_jmv423.py
    Author: Jordan Vani
    Date created: 09/17/2016
    Date last modified: 09/17/2013
    Python Version: 3.5.1
'''

import sys
import json
import urllib.request as ulr

#userkey = '0668523f-40d2-4449-a006-332eaa2f8523'

userkey = sys.argv[1]
busnum = sys.argv[2]

url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key='+userkey+'&LineRef=MTA%20NYCT_'+busnum

##Get MTA bus time data.
response = ulr.urlopen(url)
charset = response.info().get_content_charset()
data = response.read().decode(charset)
data = json.loads(data)

##Print locaiton of active buses.
vehicles = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
buscount = (len(vehicles))
print ("Bus Line : {}".format(busnum))
print ("Number of Active Buses : {}".format(buscount))
for x in range(buscount):
    print ("Bus {} is at latitude {} and longitude {}".format(x+1, vehicles[x]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], vehicles[x]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
