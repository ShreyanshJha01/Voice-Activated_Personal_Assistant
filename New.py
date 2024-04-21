import requests
from sapi import *
#S_API is another package which contains the following variable 'key'.
#The variable 'key' stores the API of the user and can't be shared due to security reasons
api_address="https://newsapi.org/v2/top-headlines?country=us&apiKey="+key
json_data = requests.get(api_address).json()
ar=[]
def news():
    for i in range(3):
        ar.append("Number "+ str(i+1) + ": " + json_data["articles"][i]["title"]+".")
    return ar
