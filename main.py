# TODO: HTTP REQUESTS
    # Get = requests.get()
        # We request information from the External system
    # Post = requests.post()
        # Send information to the external system
    # put = requests.put()
        # Update values
    # delete = requests.delete()
        # delete values

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

# response = requests.post(url=pixela_endpopoint, json=user_params)

# TODO: Advanced Authentication using an HTTP Header

graph_endpoint = f"{pixela_endpopoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "mi",
    "type": "float",
    "color": "momiji",
}
    # Headers: Like logos or numbers on a newsletter. Something that stays the same across the project.
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


# TODO: ADD A PIXEL TO THE HABIT TRACKER USING A POST REQUEST

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()


pixel_config = {
    "date": today.strftime("%Y%m%d"), # Rearange the time so it fits correctly
    "quantity": input("How many miles did you walk today?"),
}

# pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(pixel_response.text)

#TODO: How to use HTTP Put and Delete Requests
    # HTTP Put:
pixel_update_endpoint = f"{pixel_endpoint}/20230101"

pixel_update_list = {
    "quantity": "10",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_list, headers=headers)
# print(response.text)

    # HTTP Delete
pixel_delete_endpoint = f"{pixel_update_endpoint}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)

