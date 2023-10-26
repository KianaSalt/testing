import urllib.request, json
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)             # create an app instance

@app.route("/")                   # use the home url
def hello():                      # method called hello

    url = "https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation"

    querystring = {"cityName":"Berlin","countryName":"Germany"}

    headers = {
	"X-RapidAPI-Key": "38aba8fdd7msh17e0b0cef497d80p12ff81jsnae1951e99dcd",
	"X-RapidAPI-Host": "best-booking-com-hotel.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return render_template("index.html", datum=data)

if __name__ == '__main__':
    app.run(debug=True) 

 
    #print(response.json())