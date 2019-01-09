from django.shortcuts import render

def getEnviro():
    import json, requests

    URLENVIRO = 'http://10.0.1.125:8000/enviro'

    result = requests.get(URLENVIRO)
    data = json.loads(result.text)
    dataValues = json.loads(data['enviro'])
    for value in dataValues['enviro']:
        temperature = value['temperature']
        humidity = value['humidity']

    return temperature, humidity

def rooms(request):

    temperature, humidity = getEnviro()

    context = {
        'nbar': 'rooms',
        'temperature': round(temperature, 2),
        'humidity': round(humidity, 1)
    }
    return render(request, 'rooms/rooms.html', context)
