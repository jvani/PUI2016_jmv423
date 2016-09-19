'''
    File name: get_bus_info_jmv423.py
    Author: Jordan Vani
    Date created: 09/17/2016
    Date last modified: 09/17/2013
    Python Version: 3.5.1
'''

import sys
import json
import urllib.request as ulr
import pandas as pd

#userkey = '0668523f-40d2-4449-a006-332eaa2f8523'

userkey = sys.argv[1]
busnum = sys.argv[2]
outputfile = sys.argv[3]

url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key='+userkey+'&LineRef=MTA%20NYCT_'+busnum

##Get MTA bus time data.
response = ulr.urlopen(url)
charset = response.info().get_content_charset()
data = response.read().decode(charset)
data = json.loads(data)

##Write location of active buses to csv.
vehicles = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
buscount = (len(vehicles))
df = pd.DataFrame([], columns=list(['Latitude','Longitude','Stop Name','Stop Status']))
for x in range(buscount):
    latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][x]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][x]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    stopname = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][x]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
    if not stopname:
        stopname = 'N/A'
    stopstatus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][x]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
    if not stopstatus:
        stopstatus = 'N/A'
    df.loc[len(df)] = [latitude, longitude, stopname, stopstatus]
df.to_csv(path_or_buf = outputfile)
print('Requested bus info has been written to csv.')
print(df)
