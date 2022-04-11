from pprint import pprint
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "3hAwfgJ7Xy5DiLTIsAWarc1MUvFL9ARL"

class FlightSearch:
    
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        return response.json()["locations"][0]["code"]

    def check_flights(self, origin_code, destination_code, from_date, to_date, price_to):
        location_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "price_to": price_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)

        try:
            data = response.json()["data"][0]
        except:
            query["max_stopovers"] = 1
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            try:
                data = response.json()["data"][0]
                flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"])
                return flight_data
            except:
                return

        print(f"Price: {data['price']}, Origin City: {data['cityFrom']}, Origin Airpot: {data['flyFrom']}, Destination City: {data['cityTo']}, Destination Airpot: {data['flyTo']}, Out Date: {data['route'][0]['local_departure'].split('T')[0]}, Return Date: {data['route'][1]['local_departure'].split('T')[0]}")
        
        flight_data = FlightData(price=data["price"],
        origin_city=data['cityFrom'], origin_airport=data['flyFrom'], destination_city=data['cityTo'], destination_airport=data['flyTo'], out_date=data['route'][0]['local_departure'].split('T')[0], return_date=data['route'][1]['local_departure'].split('T')[0],booking_link=data['deep_link'])

        return flight_data