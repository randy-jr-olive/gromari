from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rooms.models import SensorData, Room, Plant, Journal, Tag
from rooms.forms import RoomForm, PlantForm, JournalForm
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
            tags__text__icontains=room.name).order_by('-dateUpdated')[:20]
        room.journalEntries = journalEntries

    context = {
        'nbar': 'rooms',
        'roomList': list(rooms)
    }
    return render(request, 'rooms/rooms.html', context)


@login_required
def roomDetails(request, room_id):
    if request.method == 'POST':
        if room_id == 0:
            roomForm = RoomForm(request.POST)
        else:
            room = Room.objects.get(pk=room_id)
            roomForm = RoomForm(request.POST, instance=room)

        if roomForm.is_valid():
            # adds tag for room name if it doesn't exist
            nameTag = Tag.objects.update_or_create(
                text=roomForm.cleaned_data['name'])
            roomForm.save()
            return redirect('rooms')

    else:
        if room_id == 0:
            roomForm = RoomForm()
        else:
            room = Room.objects.get(pk=room_id)
            roomForm = RoomForm(instance=room)

    context = {
        'roomForm': roomForm,
        'nbar': 'rooms'
    }

    return render(request, 'rooms/room.html', context)


@login_required
def deleteRoom(request, room_id):
    if request.method == 'POST':
        confirmed = request.POST.get('confirmed')
        if confirmed == 'true':
            room = Room.objects.filter(pk=room_id).delete()
        else:
            print("not confirmed")
        return redirect('rooms')
    else:
        return redirect('rooms')


@login_required
def plantDetails(request, room_id, plant_id):
    if request.method == 'POST':
        if plant_id == 0:
            plantForm = PlantForm(request.POST, initial={'room_fk': room_id})
        else:
            plant = Plant.objects.get(pk=plant_id)
            plantForm = PlantForm(request.POST, instance=plant)

        if plantForm.is_valid():
            # adds tag for plant name if it doesn't exist
            nameTag = Tag.objects.update_or_create(
                text=plantForm.cleaned_data['name'])
            plantForm.save()
            return redirect('rooms')

    else:
        if plant_id == 0:
            plantForm = PlantForm(initial={'room_fk': room_id})
        else:
            plant = Plant.objects.get(pk=plant_id)
            plantForm = PlantForm(instance=plant)

    context = {
        'plantForm': plantForm,
        'nbar': 'rooms'
    }

    return render(request, 'rooms/plant.html', context)


@login_required
def deletePlant(request, plant_id):
    if request.method == 'POST':
        confirmed = request.POST.get('confirmed')
        if confirmed == 'true':
            plant = Plant.objects.filter(pk=plant_id).delete()
        else:
            print("not confirmed")
        return redirect('rooms')
    else:
        return redirect('rooms')


@login_required
def journalDetails(request, journal_id, room_tag=""):
    if request.method == 'POST':
        if journal_id == 0:
            journalForm = JournalForm(request.POST)
        else:
            journal = Journal.objects.get(pk=journal_id)
            journalForm = JournalForm(request.POST, instance=journal)

        if journalForm.is_valid():
            entry = journalForm.save(commit=False)
            entry.author = request.user
            entry.save()
            journalForm.save_m2m()

            return redirect('journalHome')

    else:
        if journal_id == 0:
            if room_tag != "":
                roomNameTag = Tag.objects.filter(text__icontains=room_tag)
                journalForm = JournalForm(initial={'tags': roomNameTag})
            else:
                journalForm = JournalForm()

        else:
            journal = Journal.objects.get(pk=journal_id)
            journalForm = JournalForm(instance=journal)

    context = {
        'journalForm': journalForm,
        'nbar': 'journal'
    }

    return render(request, 'rooms/journal.html', context)


@login_required
def journalHome(request):

    journalEntries = Journal.objects.order_by('-dateUpdated')
    allTags = Tag.objects.order_by('text')

    context = {
        'nbar': 'journal',
        'journalEntries': list(journalEntries),
        'allTags': list(allTags)
    }
    return render(request, 'rooms/journal_home.html', context)


@login_required
def deleteJournalEntry(request, journal_id):
    if request.method == 'POST':
        confirmed = request.POST.get('confirmed')
        if confirmed == 'true':
            entry = Journal.objects.filter(pk=journal_id).delete()
        else:
            print("not confirmed")
        return redirect('journalHome')
    else:
        return redirect('journalHome')
