from requests import Session
import json
session = Session()
# HEAD requests ask for *just* the headers, which is all you need to grab the
# session cookie
latLngList = []
#Adrianna IS THE BESTIEST
# way 1
observations = ['2', '643', '10023']

for i in observations:
    response = session.get('http://inaturalist.org/observations/' + str(i)+'.json')
    jsonVar = json.loads(response.text)
    latLngList.append([jsonVar["latitude"], jsonVar["latitude"]])

print(latLngList)
