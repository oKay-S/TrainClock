import json
import requests
import configparser

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
      response = requests.get(
          "https://transportapi.com/v3/uk/train/station/"+ suffix +"/live.json?app_id=" + api_details["id"] + "&app_key=" + api_details["key"] + "&darwin=false&train_status=passenger")

      trains = response.json()
      departures = trains["departures"]
      all = departures["all"]

      all = all[0]
      service = all["service"]
      platform = all["platform"]
      departuretime = all["aimed_departure_time"]
      responseSecondary = requests.get(
          "https://transportapi.com/v3/uk/train/service/" + service + "///timetable.json?app_id="+ api_details["id"] + "&app_key=" + api_details["key"] + "&darwin=false&live=false")

      fullservice = responseSecondary.json()
      destination = fullservice["destination_name"]
      toc = fullservice["operator_name"]
      platform = ""
      stops = fullservice["stops"]
      looplen = len(stops)
      stoppingdestinations = []
      for i in range(looplen):
          station = stops[i]
          if i == 0:
              departuretime = station["aimed_departure_time"]
              platform = station["platform"]

              if platform is None:
                  platform = "Bus"
              else:
                  platform = "Platform: " + platform

              continue
          stationname = station["station_name"]
          arrivaltime = station["aimed_arrival_time"]
          stationinfo = stationname + " [" + arrivaltime + "]"
          stoppingdestinations.append(stationinfo)


      string1 = destination + " " + departuretime
      print(string1)
      string2 = platform
      print(string2)
      string3 = "Calling at: " + ", ".join(stoppingdestinations) + " (" + toc + ")"
      print(string3)
      finalstrings = [string1, string2, string3]
      return finalstrings