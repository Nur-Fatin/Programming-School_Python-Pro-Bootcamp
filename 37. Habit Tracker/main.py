import requests
from datetime import datetime

USERNAME = "nurbliss25"
TOKEN = "sdkjcnnejkafjh348hfjh78hjifnk"
GRAPH_ID = "graph1"

# ============Create a User Account===============#
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ============Create a New pixelation Graph===============#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Progress",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)

# ============Create a pixel: Record how many minutes I code today on the Graph ===============#

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
today_date = today.strftime("%Y%m%d")

pixel_data = {
    "date": today_date,
    "quantity": input("How many minutes you've invested in coding today? >  "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=graph_headers)

# ============Update pixel data=============== #
update_endpoint = f"{pixel_creation_endpoint}/{today_date}"

new_pixel_data = {
    "quantity": "300"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=graph_headers)
# print(response.text)

# ============Delete pixel data=============== #
delete_endpoint = f"{pixel_creation_endpoint}/{today_date}"

# response = requests.delete(url=update_endpoint, headers=graph_headers)
# print(response.text)
