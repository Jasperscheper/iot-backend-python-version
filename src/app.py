from containers import Container


from flask import Flask

from views.index import index
from views import alarmclocks
from flask_cors import CORS

def create_app() -> Flask:
    container = Container()

    app = Flask(__name__)
    CORS(app)
    cors = CORS(app, resources={
        r"/*":{
            "origins":"*"
        }
    })
    app.container = container
    app.add_url_rule("/", "index", index)
    app.add_url_rule("/alarms", "alarms_index", alarmclocks.index)
    app.add_url_rule("/alarms/registeralarm", "registerdevice", alarmclocks.RegisterAlarm.as_view("registerAlarm"))
    app.add_url_rule("/alarms/<macAddress>", "alarms_detail", alarmclocks.AlarmDetail.as_view("alarmDetail"))
    app.add_url_rule("/alarms/<macAddress>/setLocation", "alarms_setlocation", alarmclocks.SetLocation.as_view("setLocation"))
    app.add_url_rule("/alarms/<macAddress>/weather", "alarm_getweather", alarmclocks.WeatherView.as_view("getWeather"))
    return app

create_app()