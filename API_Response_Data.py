#API Response Data: APIs return data. we can convert response into JSON format, which is a common data format used for APIs.
import requests
response = requests.get("https://api.github.com")
data = response.json()
print(data)