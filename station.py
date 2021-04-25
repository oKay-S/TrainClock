import json
import requests


class Station: #Constructs the station class
  suffix = ""
  ntrain = ""
  def updateStation(): #Constructs  the Update Station Method
    f = open("config.txt", "r")
    suffix = (f.read(3))
    f.close()
    return suffix

  def updateTrains():
      suffix = Station.updateStation()
      response = requests.get(
          "https://transportapi.com/v3/uk/train/station/"+ suffix +"/live.json?app_id=d8e690f5&app_key=a64dcf1d1dd8d45481bd33c43bafe55a&darwin=false&train_status=passenger")

      trains = response.json()
      stationName = trains["station_name"]
      departures = trains["departures"]
      all = departures["all"]
      all = all[0]
      toc = all["operator_name"]
      departureTime = all["aimed_departure_time"]
      destination = all["destination_name"]

      finalString = f"The next train is the {departureTime} {toc} service to {destination}"

      return finalString