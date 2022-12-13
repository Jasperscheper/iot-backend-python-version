from flask import request, jsonify

from dependency_injector.wiring import inject, Provide
from interfaces.deviceservice import DeviceServiceInterface
from containers import Container

from devices.alarmclock import AlarmClock

from flask.views import View, MethodView

import json

class RegisterAlarm(View):
    
    methods = ['POST']
    
    @inject
    def dispatch_request(self, service: DeviceServiceInterface = Provide[Container.DeviceService]):
        body = request.json
        macAddress = body.get('macAddress')
        
        #create an alarm clock using the factory (for DI)
        alarm = Container.alarmclock_factory(macAddress)
        service.registerDevice(alarm)
            
        return "ok"
    
class AlarmDetail(MethodView):
    @inject
    def get(self, macAddress, service: DeviceServiceInterface = Provide[Container.DeviceService]):
        return json.dumps(service.fetchDevice(macAddress).toJson(), indent=4)
    
class SetLocation(MethodView):
    @inject
    def get(self, macAddress, service: DeviceServiceInterface = Provide[Container.DeviceService]):
        args = request.args
        device = service.fetchDevice(macAddress)
        device.location = args.get('location')
        
        return "ok"
    
class WeatherView(MethodView):
    @inject
    def get(self, macAddress, service: DeviceServiceInterface = Provide[Container.DeviceService]):
        device = service.fetchDevice(macAddress)
        
        if device:
            if(device.location):
                return json.dumps(device.get_weatherinfo())
            return "error; location is not set"
        
        return "Device not found"

@inject
def index(service: DeviceServiceInterface = Provide[Container.DeviceService]):
    return json.dumps(service.fetchAll(),indent=4)
    