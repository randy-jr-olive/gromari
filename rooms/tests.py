from django.test import Client, TestCase
from django.urls import reverse, resolve
from rooms.views import rooms
from django.contrib.auth.models import User
from rooms.tasks import createEnviroReadingTask
from rooms.models import SensorData, Room
import unittest
import pytest


class RoomTests(TestCase):

    client = Client()

    def setUp(self):
        # creates a test user to check login/logout functionality
        self.user = User.objects.create_user(
            username='testuser', password='12345')

    def testLoginRequired(self):
        # tests to make sure that the user must login first and will be redirected
        # to the login page from any URL they try to access without login

        response = self.client.get(reverse('rooms'))
        self.assertEqual(response.status_code, 302)

    def testLogin(self):
        # tests to make sure that the user can login and access the rooms page

        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('rooms'))
        self.assertEqual(response.status_code, 200)

    def testRoomsURLFunction(self):
        # checks if the URL 'rooms' reolves the correct rooms function

        found = resolve(reverse('rooms'))
        self.assertEqual(found.func, rooms)

    def testResponseContainsCorrectText(self):

        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('rooms'))
        self.assertContains(response, "<title>gromari - Rooms</title>")


class TaskTests(unittest.TestCase):

    def setUp(self):
        Room.objects.create(name="testing", description="testing room",
                            lightsOn=1, lightsOff=2)

    @pytest.mark.django_db(transaction=True)
    def testCreateEnviroReadingTask(self):
        testRoom = Room.objects.get(name="testing")

        createEnviroReadingTask(testRoom.id)

        latestReading = SensorData.objects.filter(
            room_fk=testRoom.id).latest('timestamp')

        self.assertIsInstance(latestReading, SensorData)
