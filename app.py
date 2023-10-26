import urllib.request, json
from flask import Flask, render_template, request
import requests

app = Flask(__name__)             # create an app instance

@app.route("/")                   # use the home url
def hello():                      # method called hello
    url = "https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation"

    querystring = {"cityName":"Berlin","countryName":"Germany"}

    headers = {
	"X-RapidAPI-Key": "4894c3a1bcmshd133c8566ef57e7p1c5692jsn39cf5eb18188",
	"X-RapidAPI-Host": "best-booking-com-hotel.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)
    data = response.read(response)
    dict = json.loads(data)
    return render_template("index.html", datum=dict)
    #print(response.json())