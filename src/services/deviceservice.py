from dependency_injector.wiring import inject

from interfaces.repository import RepositoryInterface
from interfaces.alarmclock import AlarmClockInterface
from interfaces.deviceservice import DeviceServiceInterface

@inject
class DeviceService(DeviceServiceInterface):
    
    _repository: RepositoryInterface
    
    def __init__(self, repository: RepositoryInterface):
        self._repository = repository
        
    def registerDevice(self, device: AlarmClockInterface):
        #check if we do not have this device already
        if self.fetchDevice(device.macAddress) is None:
            self._repository.insert(device)
        
    def fetchDevice(self, macAddress):
        return self._repository.fetch(macAddress)
        
    def removeDevice(self, device: AlarmClockInterface):
        self._repository.delete(device.macAddress)
        
    def fetchAll(self):
        return self._repository.fetchAll() 
        