import requests
from datetime import datetime

USERNAME = "nurfatin"
TOKEN = "vvdvdf2344r3Cfbfere"
GRAPH_ID = "graph1"

today = datetime.now()
today_date = today.strftime("%Y%m%d")

total_pages = input("How many pages did you read today?  ")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_CREATION_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
PIXEL_UPDATE_ENDPOINT = f"{PIXEL_CREATION_ENDPOINT}/{today_date}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# 1. Create my user account:
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# 2. Create a new graph
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(url=GRAPH_ENDPOINT, headers=headers, json=graph_config)
# print(response.text)

# 3. Post the value to the graph
new_pixel = {
    "date": today_date,
    "quantity": total_pages,
}

response = requests.post(url=PIXEL_CREATION_ENDPOINT, headers=headers, json=new_pixel)
print(response.text)

# 4. Update Pixel

pixel_update = {
    "quantity": "10"
}

# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, headers=headers, json=pixel_update)
# print(response.text)

# 5. Delete Pixel
# response = requests.delete(url=PIXEL_UPDATE_ENDPOINT, headers=headers)
# print(response.text)
