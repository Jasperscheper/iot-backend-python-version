#!/usr/bin/env python
import pika
import uuid
import json

#mock alarmclock object

#it has a boot and shutdown method

class AlarmClock(object):
    def __init__(self):
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue='test')

    def boot(self):
        
        params = {
            'macAddress': str(uuid.uuid4())
        }
        
        self._channel.basic_publish(exchange='', routing_key='register',  body=json.dumps(params))

        print('booted successfully')
    def shutDown(self):
        self._connection.close()
    

if __name__ == '__main__':
    
    alarmClock = AlarmClock()
    alarmClock.boot()
    alarmClock.shutDown()
