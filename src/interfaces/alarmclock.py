from abc import ABC, abstractmethod
from interfaces.weatherservice import WeatherServiceInterface

class AlarmClockInterface(ABC):

    _macAddress: str
    _weatherService: WeatherServiceInterface
    location: str
        
    