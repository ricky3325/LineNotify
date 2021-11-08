import requests
from requests.structures import CaseInsensitiveDict

url = "https://notify-api.line.me/api/notify"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer rmLp7qZyFK2hp7UCZ51Eo4CzC7hMwldghcxfnSFG8wH"
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "message=Hello World"


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
