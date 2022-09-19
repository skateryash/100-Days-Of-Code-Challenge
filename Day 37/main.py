import os
import requests
from datetime import datetime

USERNAME = "skateryash"
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Coding",
    "unit": "Hrs",
    "type": "float",
    "color": "ajisai",
    "timezone": "IST"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()
date = today.strftime("%Y%m%d")

pixel_data = {
    "date": date,
    # "quantity": input("How many hours did you practice coding today? "),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"

pixel_update_data = {
    # "quantity": "4.2",
    "timezone": "IST"
}

# response = requests.post(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"

# response = requests.post(url=delete_endpoint, headers=headers)
# print(response.text)
