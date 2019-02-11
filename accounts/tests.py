from django.test import Client, TestCase, LiveServerTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountTests(TestCase):

    client = Client()

    def setUp(self):
        # creates a test user to use for testing
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

    def testLogout(self):
        # tests to ensure a user can logout using the logout URL
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertContains(response, '<h2>You have been logged out</h2>')

    def testCreateUser(self):
        # creates a new user, then tests to make sure that user was created
        self.user = User.objects.create_user(
            username='testcreateuser', email="testing@testing.com", password='12345')
        self.assertEqual(self.user.email, "testing@testing.com")

    def testProfilePage(self):
        # checks that the profile page displays correctly
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('profile'))
        self.assertContains(
            response, '<h2 class="account-heading">testuser</h2>')

    def testRegisterPage(self):
        # checks that the register page displays correctly
        response = self.client.get(reverse('register'))
        self.assertContains(
            response, '<legend class="border-bottom mb-4">Join Today</legend>')


class RegisterFormSubmitTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.username = 'register'
        cls.email = 'register@register.com'
        cls.password = 'ThisIsAPassword1234'
        options = Options()
        options.headless = True
        cls.browser = webdriver.Firefox(options=options)
        cls.browser.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def testRegisterNewUser(self):

        self.browser.get('%s%s' % (self.live_server_url, '/register'))
        self.assertIn(
            '<legend class="border-bottom mb-4">Join Today</legend>', self.browser.page_source)

        # finds form elements, waits for them to be located
        usernameField = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_username"))).send_keys(self.username)
        emailField = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_email"))).send_keys(self.email)
        password1Field = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_password1"))).send_keys(self.password)
        password2Field = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_password2"))).send_keys(self.password)

        # submit the form
        submitButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "submit"))).click()

        # checks that the new user was created in the database by logging in
        # and checking the profile page
        login = self.client.login(
            username=self.username, password=self.password)
        response = self.client.get(reverse('profile'), follow=True)
        searchString = '<h2 class="account-heading">' + self.username + '</h2>'
        self.assertContains(response, searchString)
