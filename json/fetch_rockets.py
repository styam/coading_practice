"""
Fetch all the non repeted names of the rockets
https://api.spacexdata.com/v3/launches
"""


import requests
import json


def fetch_unique_rockets():
    URL = "https://api.spacexdata.com/v3/launches"
    request = requests.get(url=URL ).json()
    # data = request.json()
    res = list(set(i['rocket']['rocket_name'] for i in request))
    return res


print(fetch_unique_rockets())
