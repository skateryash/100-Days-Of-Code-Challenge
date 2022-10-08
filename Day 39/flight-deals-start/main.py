# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.read_sheet()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "BOM"

print("Welcome to Angel's Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name\n")
email = input("What is your email?\n")
confirm_email = input("Type your email again.?\n")
if email == confirm_email:
    print("You're in the club!")


if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.find_iata_code(row["city"])
    data_manager.sheet_data = sheet_data
    data_manager.update_sheet()

tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months,
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message_body=f"Low price alert! Only ₹{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, "
                    f"from {flight.out_date} to {flight.return_date}."
        )
