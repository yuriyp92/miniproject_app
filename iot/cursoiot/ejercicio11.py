import urequests as requests
import json

id_ciudad = "766273"
r = requests.get("https://www.metaweather.com/api/location/{}/".format(id_ciudad))
print(r.status_code)
content = r.content.decode()
print(content)

data = json.loads(r.content.decode())
wind_speed = data["consolidated_weather"][1]["wind_speed"]
print(wind_speed)