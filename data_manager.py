from pprint import pprint
from urllib import request
import requests

SHEETY_PRICES_URL = "https://api.sheety.co/35a6ae652c21441f2472693f713b27de/flightDeals/prices"
SHEETY_USERS_URL = "https://api.sheety.co/35a6ae652c21441f2472693f713b27de/flightDeals/users"

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response =  requests.get(url=SHEETY_PRICES_URL)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_URL}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def update_booking_link(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "bookingLink": city["bookingLink"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_URL}/{city['id']}",
                json=new_data
            )
            print(response.text)
    
    def get_user_data(self):
        response = requests.get(url=SHEETY_USERS_URL)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data