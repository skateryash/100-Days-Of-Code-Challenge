import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/a1ce99ba2602220bd65c82a7dd0ac763/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.sheet_data = {}

    # Reading data from Sheet
    def read_sheet(self):
        sheet_response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = sheet_response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data

    # Update data to Sheet
    def update_sheet(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheet_response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            # print(sheet_response.text)

