from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rooms.models import SensorData, Room, Plant, Journal, Tag
from rooms.forms import RoomForm, PlantForm
import json


@login_required
def rooms(request):

    rooms = Room.objects.order_by('name')

    for room in rooms:
        # loops through each room and adds xtra info to the results from
        # connected tables

        # add extra plant info for each room
        plantCount = Plant.objects.filter(room_fk=room.id).count()
        plants = Plant.objects.filter(room_fk=room.id).order_by('name')
        room.plantCount = plantCount
        room.plants = plants

        # add sensor readings for each room
        allSensorData = SensorData.objects.filter(
            room_fk=room.id).order_by('-timestamp')

        temperatureHistory = [str(reading.temperature)
                              for reading in allSensorData]
        humidityHistory = [str(reading.humidity) for reading in allSensorData]

        room.temperatureHistory = json.dumps(temperatureHistory)
        room.humidityHistory = json.dumps(humidityHistory)

        # add journal entries for each room

        journalEntries = Journal.objects.filter(
            tags__text__icontains=room.name).order_by('-dateUpdated')
        room.journalEntries = journalEntries

    context = {
        'nbar': 'rooms',
        'roomList': list(rooms)
    }
    return render(request, 'rooms/rooms.html', context)


@login_required
def roomDetails(request, id=-1):
    if request.method == 'POST':
        if id == -1:
            roomForm = RoomForm(request.POST)
        else:
            room = Room.objects.get(pk=id)
            roomForm = RoomForm(request.POST, instance=room)

        if roomForm.is_valid():
            roomForm.save()
            return redirect('rooms')

    else:
        if id == -1:
            roomForm = RoomForm()
        else:
            room = Room.objects.get(pk=id)
            roomForm = RoomForm(instance=room)

    context = {
        'roomForm': roomForm,
        'nbar': 'rooms'
    }

    return render(request, 'rooms/room.html', context)


@login_required
def deleteRoom(request, id):
    if request.method == 'POST':
        confirmed = request.POST.get('confirmed')
        if confirmed == 'true':
            room = Room.objects.filter(pk=id).delete()
        else:
            print("not confirmed")
        return redirect('rooms')
    else:
        return redirect('rooms')


@login_required
def plantDetails(request, id=-1):
    if request.method == 'POST':
        if id == -1:
            plantForm = PlantForm(request.POST)
        else:
            plant = Plant.objects.get(pk=id)
            plantForm = PlantForm(request.POST, instance=plant)

        if plantForm.is_valid():
            plantForm.save()
            return redirect('rooms')

    else:
        if id == -1:
            plantForm = PlantForm()
        else:
            plant = Plant.objects.get(pk=id)
            plantForm = PlantForm(instance=plant)

    context = {
        'plantForm': plantForm,
        'nbar': 'rooms'
    }

    return render(request, 'rooms/plant.html', context)


@login_required
def deletePlant(request, id):
    if request.method == 'POST':
        confirmed = request.POST.get('confirmed')
        if confirmed == 'true':
            plant = Plant.objects.filter(pk=id).delete()
        else:
            print("not confirmed")
        return redirect('rooms')
    else:
        return redirect('rooms')
