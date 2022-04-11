from data_manager import DataManager
from notification_manager import NotificationManager
from pprint import pprint
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search =  FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    pprint(f"Updated Sheet Data:\n{sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

for row in sheet_data:
    from flight_search import FlightSearch
    flight_search =  FlightSearch()

    flight_data = flight_search.check_flights("LON", row["iataCode"], datetime.now(), datetime.now() + timedelta(days=180), row["lowestPrice"])

    try:
        flight_price = flight_data.price
    except:
        print(f"Flight Not Found for {row['iataCode']}")
        continue

    row["bookingLink"] = flight_data.booking_link

    users = data_manager.get_user_data()
    emails = [row["email"] for row in users]
    names = [row["firstName"] for row in users]

    message = f"Flight from {flight_data.origin_city} to {flight_data.destination_city} is available at low price of {flight_data.price}"
    notification_manager = NotificationManager()
    notification_manager.send_emails(emails, names, message, flight_data.booking_link)

pprint(f"Updated Sheet Data:\n{sheet_data}")

data_manager.update_booking_link()