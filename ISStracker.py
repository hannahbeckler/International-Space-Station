import json
import requests
import time

endpoint = "http://api.open-notify.org/iss-now.json"
parameters = {}

result = requests.get(endpoint,params=parameters)

print (result.status_code)
print (result.headers)
print (result.text)
resultdict = json.loads(result.text)
print()
timestamp = resultdict['timestamp']
print (timestamp)
positiondict = resultdict['iss_position']
print ()
print (positiondict)

outfile = open('isspause.txt','w')
number = 30
delay = 2
for i in range(0,number):
    result = requests.get(endpoint,params=parameters)
    resultstring = result.text
    resultdict = json.loads(resultstring)
    positiondict = resultdict['iss_position']
    print (positiondict['latitude'],positiondict['longitude'], file = outfile)
    print ("Iteration",i,"of",number)
    outfile.flush()
    time.sleep(delay)

outfile.close()
