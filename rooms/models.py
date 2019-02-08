from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    # Model of information related to an individual grow room

    name = models.CharField(max_length=200)
    description = models.TextField()
    lightsOn = models.IntegerField(default=0)
    lightsOff = models.IntegerField(default=1)
    activeSensor = models.BooleanField(default=False)
    currentTemperature = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    currentHumidity = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        # Sets the plural form for display in the django admin app
        verbose_name_plural = "Rooms"

    def __str__(self):
        # Sets the string that is returned on the list for this model on the
        # django admin page
        return self.name

    def getRooms(self):
        # returns a queryset of all rooms
        return Room.objects.all()

    def getRoom(self, room):
        # returns a single room
        return Room.objects.get(pk=room)


class Plant(models.Model):
    # Model of information related to an individual plant in a room

    name = models.CharField(max_length=200, unique=True)
    species = models.CharField(max_length=200)
    datePlanted = models.DateTimeField()
    description = models.TextField()

    # foreign key of the room that houses this plant
    room_fk = models.ForeignKey('Room', on_delete=models.CASCADE)

    class Meta:
        # Sets the plural form for display in the django admin app
        verbose_name_plural = "Plants"

    def __str__(self):
        # Sets the string that is returned on the list for this model on the
        # django admin page
        return self.name


class Tag(models.Model):
    # Model of information related to an individual tag

    text = models.CharField(max_length=250)

    class Meta:
        # Sets the plural form for display in the django admin app
        verbose_name_plural = "Tags"

    def __str__(self):
        # Sets the string that is returned on the list for this model on the
        # django admin page
        return self.text


class Journal(models.Model):
    # Model of information related to an individual journal entry

    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        # Sets the plural form for display in the django admin app
        verbose_name_plural = "Journal Entries"

    def __str__(self):
        # Sets the string that is returned on the list for this model on the
        # django admin page
        return str(self.dateCreated)


class Equipment(models.Model):
    # Model of information related to an individual piece of equipment

    type = models.CharField(max_length=250)
    description = models.TextField()

    # foreign key of the room where this equipment is
    room_fk = models.ForeignKey('Room', on_delete=models.CASCADE)

    class Meta:
        # Sets the plural form for display in the django admin app
        verbose_name_plural = "Equipment"

    def __str__(self):
        # Sets the string that is returned on the list for this model on the
        # django admin page
        return self.type


class SensorData(models.Model):
    # Model of an individual reading from temp/RH sensor

    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00)
    humidity = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00)

    # foreign key of the room where this sensor is
    room_fk = models.ForeignKey('Room', on_delete=models.CASCADE)

    class Meta:
        # Sets the plural form for display in the django admin app
        verbose_name_plural = "Sensor Data"

    def __str__(self):
        # Sets the string that is returned on the list for this model on the
        # django admin page
        return str(self.timestamp)

    def getLatestReading(self, roomID):
        latestReading = SensorData.objects.filter(room_fk=roomID).latest('timestamp')
        temperature = latestReading.temperature
        humidity = latestReading.humidity

        return temperature, humidity
