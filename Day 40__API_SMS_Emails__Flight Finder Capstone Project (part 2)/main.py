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
_data_manager.get_user_data()
for city in _data_manager.city_data:
    city["iataCode"] = _flight_search.get_iata_code(city["city"])
    _flight_data.get_lowest_price("LON", city["iataCode"])

    sms = f'\nLow price alert! Only £{_flight_data.lowest_price} to fly from ' \
          f'{_flight_data.cityFrom}-{_flight_data.flyFrom} to ' \
          f'{_flight_data.cityTo}-{_flight_data.flyTo}, ' \
          f'from {_flight_data.local_departure} to {_flight_data.local_arrival}.'
    if _flight_data.stop_overs > 0:
        sms += f'\nFlight has {_flight_data.stop_overs} stopover, via {",".join(_flight_data.via_city)}.'
    print(sms)
    if _flight_data.lowest_price < city["lowestPrice"]:
        # _notification_manager.send_sms(sms)
        list_emails = []
        for person in _data_manager.user_data:
            name = person["firstName"]
            email = person["email"]
            link = f"https://www.google.co.uk/flights?hl=en#flt={_flight_data.flyFrom}.{_flight_data.flyTo}." \
                   f"{_flight_data.local_departure}*{_flight_data.flyTo}.{_flight_data.flyFrom}." \
                   f"{_flight_data.local_arrival}"
            message = f'Dear {name},\n{sms}\n{link}'
            list_emails.append({
                "email": email,
                "message": message
            })
        # _notification_manager.send_email(list_emails)

_data_manager.update_iata_code()
