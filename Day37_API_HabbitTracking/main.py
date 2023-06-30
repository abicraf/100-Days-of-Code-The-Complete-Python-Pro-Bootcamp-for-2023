import requests
from datetime import *

USER_NAME = "xxx"
TOKEN = "xxx"

# # Create user account
# user_body = {
#     "token": TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
user_end_point = "https://pixe.la/v1/users"
# response = requests.post(url=user_end_point, json=user_body)
# print(response.text)
#
# #Create Graph
# graph_body = {
#     "id": USER_NAME,
#     "name": "Hello! Let's workout!",
#     "unit": "commit",
#     "type": "int",
#     "color": "sora",
# }
# graph_header = {
#     "X-USER-TOKEN": TOKEN
# }
# graph_end_point = f"{user_end_point}/{USER_NAME}/graphs"
# response = requests.post(url=graph_end_point, json=graph_body, headers=graph_header)
# print(response.text)

# Get the Graph
graph_end_point = f"{user_end_point}/{USER_NAME}/graphs/{USER_NAME}"
# response = requests.get(url=graph_end_point)
# print(response.text)

today = datetime.now()
# today = datetime(year=2023, month=5, day=25)
# print(today.strftime("%Y%m%d"))
date = today.strftime("%Y%m%d")
# Post value to the graph
value_jason = {
    "date": date,
    "quantity": input("How many quantity you want to commit?"),
}
graph_header = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_end_point, json=value_jason, headers=graph_header)
print(response.text)
#
# # change the pixel
#
# pixel_jason = {
#     "quantity": "6",
# }
# print(date)
#
# # response = requests.put(url=f"{graph_end_point}/{date}", json=pixel_jason, headers=graph_header)
# # print(response.text)
#
#
# # delete a pixel
# response = requests.delete(url=f"{graph_end_point}/{date}", headers=graph_header)
# print(response.text)