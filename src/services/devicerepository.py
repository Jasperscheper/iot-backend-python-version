from interfaces.alarmclock import AlarmClockInterface
from interfaces.repository import RepositoryInterface

class DeviceRepository(RepositoryInterface):
    
    def __init__(self):
        self._devices = []
    
    def insert(self, alarm: AlarmClockInterface):
        self._devices.append(alarm)
    
    def fetch(self, macAddress: str):
        filter = [device for device in self._devices if device.macAddress == macAddress]
        
        if(len(filter) > 0):
            return filter[0]
        
    def fetchAll(self):
        print(self._devices)
        return [device.toJson() for device in self._devices]
    
    def delete(self, macAddress):
        filter = [device for device in self._devices if device.macAddress == macAddress]
        
        if(len(filter) > 0):
            filter = filter[0]
            
        self._devices.remove(filter)