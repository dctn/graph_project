import requests
from _datetime import datetime

token = "ommbu_da"
username = "stranger2000"

pixla_endpoint = f"https://pixe.la/v1/users/{username}"

account_details = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_id  = "codinggraph1"

graphs_details = {
    "id": graph_id,
    "name": "coding_graph",
    "unit": "hour",
    "type": "float",
    "color": "momiji",
}
header = {
    "X-USER-TOKEN": token,
}

date = datetime.now()
formated_date = date.strftime("%Y%m%d")

graph_put_value = {
    "date": formated_date,
    "quantity": input("Enter how many hours you code today: "),
}

response = requests.post(url=f"{pixla_endpoint}/graphs/{graph_id}",json=graph_put_value,headers=header)

print(response.text)