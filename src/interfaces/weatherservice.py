from abc import ABC, abstractmethod

class WeatherServiceInterface(ABC):
    
    @abstractmethod
    def get_weather(self, location: str):
        pass