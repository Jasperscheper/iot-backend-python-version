from abc import ABC, abstractmethod

from interfaces.alarmclock import AlarmClockInterface
from interfaces.repository import RepositoryInterface

class DeviceServiceInterface(ABC):
    __repository: RepositoryInterface
    
    @abstractmethod
    def registerDevice(alarm: AlarmClockInterface) -> None:
        pass