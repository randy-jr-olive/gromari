from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def rooms(request):
    from rooms.models import SensorData, Room

    temperature = 0.0
    humidity = 0.0

    rooms = Room.objects.all()
    for room in rooms:
        temperature, humidity = SensorData.getLatestReading(request, room.id)

    context = {
        'nbar': 'rooms',
        'temperature': round(temperature, 1),
        'humidity': round(humidity, 1)
    }
    return render(request, 'rooms/rooms.html', context)
