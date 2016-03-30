from django.test import LiveServerTestCase
from selenium import webdriver

# Create your tests here.

class PollsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicity_wait(3)

    def tearDown(self):
        self.browser.quit()

    


