from interfaces.alarmclock import AlarmClockInterface
from datetime import date
from services.weatherservice import WeatherService

from dependency_injector.wiring import inject, Provide

class AlarmClock(AlarmClockInterface):
    
    _weatherService = None
    
    _location = None
    _macAddress = None
    
    def __init__(self, macAddress: str, weatherService: WeatherService):
        self._macAddress = macAddress
        self._weatherService = weatherService
        
        
    def get_weatherinfo(self):
        return self._weatherService.get_weather(self._location)
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        self._location = location
    
    @property
    def macAddress(self):
        return self._macAddress
    
    @macAddress.setter
    def macAddress(self, macAddress):
        self._macAddress = macAddress
        
    def toJson(self):
        return {
            'macAddress': self.macAddress,
            'location': self.location
        }