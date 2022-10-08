import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = 'LaPXOlw6Agxe-3h2bmCKlxvR-WikiDew'
TEQUILA_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:
    def find_iata_code(self, city_name):
        parameters = {
            "term": city_name
        }
        header = {
            "apikey": TEQUILA_API_KEY
        }
        # code = "TESTING"
        response = requests.get(url=TEQUILA_LOCATION_ENDPOINT, params=parameters, headers=header)
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"apikey": TEQUILA_API_KEY}
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "flight_type": "round",
            "curr": "INR"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            params=parameters,
            headers=header
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            # print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        # print(f"{flight_data.destination_city}: ₹{flight_data.price}")
        return flight_data

