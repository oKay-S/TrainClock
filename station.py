import json
import requests
import configparser

from requests.auth import HTTPBasicAuth

config = configparser.ConfigParser()		
config.read("config.ini")

api_details = config["API"]
station_details = config["STATION"]

class Station: #Constructs the station class
  suffix = ""
  ntrain = ""
  def updateStation(): #Constructs  the Update Station Method
    return station_details["station"]

  def updateTrainsCalling():
      suffix = Station.updateStation()
      url = "https://api.rtt.io/api/v1/json/search/" + suffix
      response = requests.get(url, auth=HTTPBasicAuth(api_details['id'], api_details['key']))

      trains = response.json()
      trains = trains['services']
      train = trains[0]
      toc = train['atocName']
      destinationDetail = train['locationDetail']
      platform = destinationDetail['platform']
      departure = destinationDetail['gbttBookedDeparture']
      destinationName = destinationDetail['destination']
      destinationName = destinationName[0]
      destinationName = destinationName['description']


      string1 = destinationName + " " + departure
      print(string1)
      string2 = "Platform " + platform
      print(string2)
      string3 = "This is a " + toc + " service"
      print(string3)
      finalstrings = [string1, string2, string3]
      return finalstrings