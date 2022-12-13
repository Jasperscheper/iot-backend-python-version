import requests
import urllib.parse
from interfaces.weatherservice import WeatherServiceInterface

class WeatherService(WeatherServiceInterface):

    #memoize the results
    _results = {}
    
    def get_weather(self, location: str):
        
        if location not in self._results:
            #get lat long based on location str
            lat, lon = self.get_lat_long(location)
            #get from a free weather api
            result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m").json()
            self._results[location] = result
            
        return self._results[location]
        
    def get_lat_long(self, location):
        #we return the lat long from openstreetmap using the location search string
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) +'?format=json'
        response = requests.get(url).json()

        #return a tuple with lat long
        return (response[0]["lat"], response[0]["lon"])