#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

_data_manager = DataManager()
_flight_search = FlightSearch()
_flight_data = FlightData()
_notification_manager = NotificationManager()

_data_manager.get_city_data()
for city in _data_manager.city_data:
    city["iataCode"] = _flight_search.get_iata_code(city["city"])
    _flight_data.get_lowest_price("LON", city["iataCode"])
    print(f"{_flight_data.cityTo} - {_flight_data.lowest_price}")
    if _flight_data.lowest_price < city["lowestPrice"]:
        sms = f'\nLow price alert! Only £{_flight_data.lowest_price} to fly from ' \
              f'{_flight_data.cityFrom}-{_flight_data.flyFrom} to {_flight_data.cityTo}-' \
              f'{_flight_data.flyTo}, from {_flight_data.local_departure} to {_flight_data.local_arrival}.'
        _notification_manager.send_sms(sms)

_data_manager.update_iata_code()
