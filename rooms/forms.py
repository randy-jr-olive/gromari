from django import forms
from .models import Room, Plant


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('name', 'description', 'lightsOn',
                  'lightsOff', 'activeSensor')


class PlantForm(forms.ModelForm):

    class Meta:
        model = Plant
        fields = ('name', 'species', 'description', 'datePlanted', 'room_fk')

    name = forms.CharField(max_length=200, label="Plant Name")
    species = forms.CharField(max_length=200, label="Species")
    description = forms.CharField(label="Description")
    datePlanted = forms.DateTimeField(label="Date Planted")
    room_fk = forms.ModelChoiceField(queryset=Room.objects.all(), label="Room")
