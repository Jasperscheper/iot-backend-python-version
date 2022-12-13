from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from services.devicerepository import DeviceRepository
from services.deviceservice import DeviceService

from services.weatherservice import WeatherService

from devices.alarmclock import AlarmClock

class Container(containers.DeclarativeContainer):
    
    #specify where we want to inject our dependencies
    wiring_config = containers.WiringConfiguration(modules=["views.alarmclocks"])

    config = providers.Configuration()
    
    DeviceRepository = providers.Singleton(
        DeviceRepository
    )
    
    DeviceService = providers.Factory(
        DeviceService, repository = DeviceRepository
    )
    
    alarmclock_factory = providers.Factory(
        AlarmClock, weatherService = WeatherService()
    )
    
    WeatherService =providers.Singleton(
        WeatherService
    )
    

