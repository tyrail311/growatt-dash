import growattServer
from pprint import pprint

gw = growattServer.GrowattApi()
gw.server_url='https://server-us.growatt.com/'
login_response = gw.login('patrick.h.nadeau', 'mitvug-xurdoz-8coZdy')
plant = gw.plant_list(login_response['user']['id'])
print(plant)
plant_id = plant['data'][0]['plantId']
pprint(plant_id)
plant_data = gw.plant_info(plant_id)
pprint(plant_data)