import growattServer
from pprint import pprint
import datetime
gw = growattServer.GrowattApi()
gw.server_url='https://server-us.growatt.com/'
login_response = gw.login('patrick.h.nadeau', 'mitvug-xurdoz-8coZdy')
plant = gw.plant_list(login_response['user']['id'])
plant_id = plant['data'][0]['plantId']
plant_data = gw.plant_info(plant_id)
inverters = gw.inverter_list(plant_id)
inverter_sns = []

for sn in range(0, 4):
    inverter_sn = inverters[sn]['deviceSn']
    inverter_sns.append(str(inverter_sn))

# for sn in inverter_sns:
#     print(f'Serial Number: {sn}')
#     inverter_data = gw.inverter_detail(sn)
#     pprint(inverter_data)


# date1 = datetime.strptime(date, '%Y-%m-%d')
# pprint(gw.inverter_data(inverter_sns[0], datetime.strftime(date1, '%Y-%m-%d %H:%M:%S')))
# cr_date = datetime(2022, 10, 31)
# print(type(cr_date))
# cr_date.strftime('%m/%d/%Y')

pprint(gw.inverter_data(inverter_sns[0], date=datetime.datetime(2022, 12, 20).date()))
# print(inverter_sns[0])

