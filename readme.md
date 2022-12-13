# IOT Python backend

Get started:

First, create a virtualenvironment (or not...):

```python3 -m venv venv```

After that, install the required dependencies:

```pip install -r requirements.txt```

Run the rabbitMQ server:

``` docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management ```

After that run the flask server:

````flask run```

Now we are ready to mock the devices:

to run the alarm register listener run:

```python registerlistener.py```

This will listen on the mqtt register topic for new handshakes.

to bootup an alarmclock run

``` testing/alarmclock.py```

Now we should be able to see the alarms:

```localhost:5000/alarms```


