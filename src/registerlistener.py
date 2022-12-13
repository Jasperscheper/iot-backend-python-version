import pika
import sys
import json
import requests
import os

from dotenv import load_dotenv


class RegisterListener(object):
    
    channel = None
    
    def __init__(self):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue='register')    
        self._channel.basic_consume(queue="register", auto_ack=True, on_message_callback=self.registerDevice)
        
        print(' [*] Waiting for messages...')
        self._channel.start_consuming()
        
    def registerDevice(self, ch, method, properties, body):
        print("Received register request...")
        #no validation here (yet):
        requests.post(os.environ.get("REGISTER_URL"), json=json.loads(body))
        

if __name__ == '__main__':
    try:
        
        load_dotenv()
        RegisterListener()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
