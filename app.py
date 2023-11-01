import urllib.request, json
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)             # create an app instance

@app.route("/")                   # use the home url
def hello():                      # method called hello

    url = "https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation"

    querystrings = [
    {"cityName": "Berlin", "countryName": "Germany"},
    {"cityName": "Atlanta", "countryName": "Georgia"},
    {"cityName": "Bangkok", "countryName": "Thailand"}
    ]
   #querystring = {"cityName":"Berlin","countryName":"Germany"}
    #querystring2 = {"cityName":"Atlanta","countryName":"Georgia"}

    headers = {
	"X-RapidAPI-Key": "f483517b4amshef1d273499a38dep145e52jsn49c64fb576fb",
	"X-RapidAPI-Host": "best-booking-com-hotel.p.rapidapi.com"
    }
    all_data = []

    for querystring in querystrings:
        response = requests.get(url, headers=headers, params=querystring)

    #data = response.json()
        #if response.status_code != 200:
            #return f"Error: Received status code {response.status_code} from API."
        data = response.json()
        all_data.append(data)
    return all_data

# Display the data
    for item in all_data:
        print(item)

    #response = requests.get(url, headers=headers, params=querystring)
    #data = response.json()
    #return render_template("index.html", datum=data)

if __name__ == '__main__':
    app.run(debug=True) 

 
    #print(response.json())