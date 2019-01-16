from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def getEnviro():
    import json
    import requests

    URLENVIRO = 'http://10.0.1.125:8000/enviro'

    result = requests.get(URLENVIRO)
    data = json.loads(result.text)
    dataValues = json.loads(data['enviro'])
    temperature = dataValues['enviro'][0]['temperature']
    humidity = dataValues['enviro'][0]['humidity']

    return temperature, humidity


@login_required
def rooms(request):

    temperature, humidity = getEnviro()

    context = {
        'nbar': 'rooms',
        'temperature': round(temperature, 2),
        'humidity': round(humidity, 1)
    }
    return render(request, 'rooms/rooms.html', context)
