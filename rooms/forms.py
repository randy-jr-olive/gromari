from django import forms
from .models import Room, Plant, Journal

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
    description = forms.CharField(label="Description", widget=forms.Textarea)
    datePlanted = forms.DateTimeField(label="Date Planted")
    room_fk = forms.ModelChoiceField(queryset=Room.objects.all(), label="Room")


class JournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ('text', 'tags', 'dateUpdated')
        exclude = ['author']

    dateUpdated = forms.DateTimeField(label="Date")
