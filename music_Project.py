import requests
from requests.exceptions import HTTPError
import json

try:
    url = "https://deezerdevs-deezer.p.rapidapi.com/search"

    querystring = {"q": "rain on me"}

    headers = {
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
        'x-rapidapi-key': "1f6d8cfeb1msh4f121c21d183941p185143jsn597044366472"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    jsonData = json.loads(response.text)

    for l in jsonData["data"]:
        print("===============")
        print(l["title"])
        print(l["artist"]["name"])
        print(l["album"]["title"])


except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
