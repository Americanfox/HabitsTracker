import requests
from datetime import datetime

USERNAME = "lukah"
TOKEN = "aassdfrhkw4h5sdh42234kd"
GRAPH_ID = "graph1"
pixela_endpopoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpopoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "mi",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()


pixel_config = {
    "date": today.strftime("%Y%m%d"), # Rearange the time so it fits correctly
    "quantity": input("How many miles did you walk today?"),
}

pixel_update_endpoint = f"{pixel_endpoint}/20230101"

pixel_update_list = {
    "quantity": "10",
}

pixel_delete_endpoint = f"{pixel_update_endpoint}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)

