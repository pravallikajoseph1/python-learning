#GET Request means: fetch/get data from a specified resource. It is one of the most common HTTP methods used to retrieve information from a server.
#In a GET request, the client sends a request to the server, and the server responds with the requested data. The data is typically sent in the response body, and the client can then process or display it as needed.
#Example: If you want to get weather data for a specific city, you can send a GET request to a weather API with the city name as a parameter. The API will then return the current weather information for that city in the response.
import requests

response = requests.get("https://api.github.com")

print(response.status_code)

#IN TERMINAL PRESS "python GET_Request.py" TO RUN THE CODE. IT WILL PRINT THE STATUS CODE OF THE RESPONSE FROM THE GITHUB API. A STATUS CODE OF 200 INDICATES THAT THE REQUEST WAS SUCCESSFUL.
# CODE 200: success
# CODE 404: not found
# CODE 500: server error
