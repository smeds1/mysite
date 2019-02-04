from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from django.test import TestCase
from django.urls import reverse
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumIndexTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(3)
        cls.selenium.get('{}{}'.format(cls.live_server_url, '/'))

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_title(self):
        """
        Make sure index load with correct title.
        """
        self.assertEqual(self.selenium.title, "Smeds Project Page")

    def test_navbar_links(self):
        """
        Make sure all links in navbar open correctly
        """
        aboutme = self.selenium.find_element_by_link_text('About Me')
        aboutme.click()
        self.assertEqual(self.selenium.title, "About Me")
        self.selenium.find_elements_by_class_name("navbar-brand")[0].click()
        basketball = self.selenium.find_element_by_link_text('Basketball Project')
        basketball.click()
        self.assertEqual(self.selenium.title, "Basketball Project")
        self.selenium.find_elements_by_class_name("navbar-brand")[0].click()
        education = self.selenium.find_element_by_link_text('Education Project')
        education.click()
        self.assertEqual(self.selenium.title, "Education Project")
        self.selenium.find_elements_by_class_name("navbar-brand")[0].click()

    def test_body_links(self):
        """
        Make sure all links in body open correctly
        """
        self.selenium.find_element_by_link_text("Kaggle's").click()
        WebDriverWait(self.selenium, 10).until(EC.number_of_windows_to_be(2))
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        self.assertEqual(self.selenium.title, "NCAA Basketball | Kaggle")
        self.selenium.close()
        self.selenium.switch_to_window(self.selenium.window_handles[0])
        self.selenium.find_element_by_link_text('U.S. Department of Education').click()
        WebDriverWait(self.selenium, 10).until(EC.number_of_windows_to_be(2))
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        self.assertEqual(self.selenium.title, "EDFacts Data Files | U.S. Department of Education")
        self.selenium.close()
        self.selenium.switch_to_window(self.selenium.window_handles[0])
        self.selenium.find_element_by_link_text("Basketball Project").click()
        self.assertEqual(self.selenium.title, "Basketball Project")
        self.selenium.find_elements_by_class_name("navbar-brand")[0].click()
        self.selenium.find_element_by_link_text("Education Project").click()
        self.assertEqual(self.selenium.title, "Education Project")
        self.selenium.find_elements_by_class_name("navbar-brand")[0].click()

class AllPagesOpen(TestCase):

    def test_index_loads(self):
        """
        Make sure main index page loads and displays content
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Me")
        self.assertContains(response, "March Madness")
        self.assertContains(response, "graduation rates")

    def test_about_me_loads(self):
        """
        Make sure about me page loads and displays content
        """
        response = self.client.get(reverse('aboutme'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Education Project")
        self.assertContains(response, "Williams")

    def test_basketball_project_loads(self):
        """
        Make basketball project main page loads and displays content
        """
        response = self.client.get(reverse('basketball:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Explore the Data")
        self.assertContains(response, "March Madness Sadness")

    def test_education_project_loads(self):
        """
        Make basketball project main page loads and displays content
        """
        response = self.client.get(reverse('education:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Demographics")
        self.assertContains(response, "How Rates Were Calculated")
