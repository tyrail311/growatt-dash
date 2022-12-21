import json
import requests
import datetime

from enum import IntEnum

class Timespan(IntEnum):
    hour = 0
    day = 1
    month = 2

def __get_date_string(timespan=None, date=None):
        if timespan is not None:
         assert timespan in Timespan

        if date is None:
          date = datetime.datetime.now()

        date_str=""
        if timespan == Timespan.month:
            date_str = date.strftime('%Y-%m')
        else:
            date_str = date.strftime('%Y-%m-%d')

        return date_str

server_url='https://server-us.growatt.com/'
def get_url(page):
        """
        Simple helper function to get the page url/
        """
        return server_url + page
def inverter_data(inverter_id, date=None):
        session = requests.Session()
        """
        Get inverter data for specified date or today.
        """
        date_str = __get_date_string(date=date)
        response = session.get(get_url('newInverterAPI.do'), params={
            'op': 'getInverterData',
            'id': inverter_id,
            'type': 1,
            'date': date_str
        })
        print(response.content.decode('utf-8'))
        data = json.loads(response.content.decode('utf-8'))
        return data
print(inverter_data('JPK1CEG0AJ', date=datetime.datetime(2022, 12, 20).date()))