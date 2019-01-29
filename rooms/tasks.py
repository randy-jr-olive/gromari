from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from django.db import connection
from time import sleep
from rooms.models import SensorData


@shared_task
def createEnviroReadingTask(roomID):
    import json
    import requests
    from rooms.models import Room

    # URL of the sensor API
    URLENVIRO = 'http://10.0.1.125:8000/enviro'

    try:
        # loops while trying to connect to API
        connected = False
        connectCounter = 0
        while connectCounter < 100:
            try:
                result = requests.get(URLENVIRO)
                connected = True
            except requests.exceptions.RequestException as e:
                print("error connecting to sensor API" + str(e))
                sleep(1.0)  # sleep timer to avoid taxing API
                pass
            if connected is True:
                break
            else:
                connectCounter += 1

        data = json.loads(result.text)
        dataValues = json.loads(data['enviro'])
        temperature = dataValues['enviro'][0]['temperature']
        humidity = dataValues['enviro'][0]['humidity']

        # get room object from roomID
        room = Room.objects.get(pk=roomID)

        reading = SensorData(temperature=temperature,
                             humidity=humidity, room_fk=room)
        reading.save()

    finally:
        connection.close()

    return


# CRONTAB periodic tasks

@periodic_task(run_every=(crontab(minute='*/1')), name="periodicCreateEnviroReadingTask", ignore_result=True)
def periodicCreateEnviroReadingTask():
    from rooms.models import Room
    rooms = Room.objects.all()
    for room in rooms:
        createEnviroReadingTask.delay(room.id)

@periodic_task(run_every=(crontab(minute='*/30')), name="periodicDeleteOldSensorDataTask", ignore_result=True)
def periodicDeleteOldSensorDataTask():
    from datetime import timedelta
    from django.utils import timezone
    from rooms.models import SensorData

    results = SensorData.objects.filter(timestamp__lt=timezone.now()-timedelta(days=1)).delete()
