from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from .models import State

STATES = ['AK','AL','AR','AZ','BI','CA','CO','CT','DC','DE','FL','GA','HI','IA',
    'ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC',
    'ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN',
    'TX','UT','VA','VT','WA','WI','WV','WY']
STATES_LONG = ['Alaska','Alabama','Arkansas','Arizona','California','Colorado','Connecticut','Delaware',
    'Florida','Georgia','Hawaii','Iowa','Idaho','Illinois','Indiana','Kansas','Kentucky',
    'Louisiana','Massachusetts','Maryland','Maine','Michigan','Minnesota','Missouri',
    'Mississippi','Montana','North Carolina','North Dakota','Nebraska','New Hampshire',
    'New Jersey','New Mexico','Nevada','New York','Ohio','Oklahoma','Oregon','Pennsylvania',
    'Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Virginia',
    'Vermont','Washington','Wisconsin','West Virginia','Wyoming']
DEMOGRAPHICS = ['White','Black','Hispanic','Asian','Native American','Multiracial',
    'Economically Disadvantaged','Children With Disabilities','English Learners']

def create_states():
    """
    Create data for the State database.
    """
    for s in STATES:
        if s < 'F':
            State.objects.create(state=s,all_cohort=1000,mam_cohort=100,mas_cohort=100,
            mbl_cohort=100,mhi_cohort=100,mtr_cohort=100,mwh_cohort=100,cwd_cohort=100,
            ecd_cohort=100,lep_cohort=100,num_schools=10,all_rate=0.9,mam_rate=0.9,
            mas_rate=0.9,mbl_rate=0.9,mhi_rate=0.9,mtr_rate=0.9,mwh_rate=0.9,
            cwd_rate=0.9,ecd_rate=0.9,lep_rate=0.9)
        elif s < 'M':
            State.objects.create(state=s,all_cohort=1000,mam_cohort=100,mas_cohort=100,
            mbl_cohort=100,mhi_cohort=100,mtr_cohort=100,mwh_cohort=100,cwd_cohort=100,
            ecd_cohort=100,lep_cohort=100,num_schools=10,all_rate=0.8,mam_rate=0.8,
            mas_rate=0.8,mbl_rate=0.8,mhi_rate=0.8,mtr_rate=0.8,mwh_rate=0.8,
            cwd_rate=0.8,ecd_rate=0.8,lep_rate=0.8)
        elif s < 'R':
            State.objects.create(state=s,all_cohort=1000,mam_cohort=100,mas_cohort=100,
            mbl_cohort=100,mhi_cohort=100,mtr_cohort=100,mwh_cohort=100,cwd_cohort=100,
            ecd_cohort=100,lep_cohort=100,num_schools=10,all_rate=0.7,mam_rate=0.7,
            mas_rate=0.7,mbl_rate=0.7,mhi_rate=0.7,mtr_rate=0.7,mwh_rate=0.7,
            cwd_rate=0.7,ecd_rate=0.9,lep_rate=0.7)
        else:
            State.objects.create(state=s,all_cohort=1000,mam_cohort=100,mas_cohort=100,
            mbl_cohort=100,mhi_cohort=100,mtr_cohort=100,mwh_cohort=100,cwd_cohort=100,
            ecd_cohort=100,lep_cohort=0,num_schools=10,all_rate=0.6,mam_rate=0.6,
            mas_rate=0.6,mbl_rate=0.6,mhi_rate=0.6,mtr_rate=0.6,mwh_rate=0.6,
            cwd_rate=0.6,ecd_rate=0.6,lep_rate=None)

class SeleniumEducationTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        create_states()
        self.selenium.get('{}{}'.format(self.live_server_url, '/education'))

    def test_navbar_links(self):
        """
        Make sure all links in navbar open correctly
        """
        self.selenium.find_elements_by_class_name("navbar-brand")[0].click()
        self.assertEqual(self.selenium.title, "Smeds Project Page")
        self.selenium.find_element_by_link_text('Education Project').click()
        self.assertEqual(self.selenium.title, "Education Project")
        self.selenium.find_element_by_link_text('States').click()
        self.assertEqual(self.selenium.title, "Education: U.S. States")
        self.selenium.find_element_by_link_text('Demographics').click()
        self.assertEqual(self.selenium.title, "Education: Demographics")
        self.selenium.find_element_by_link_text('Home').click()
        self.assertEqual(self.selenium.title, "Education Project")
        for group in DEMOGRAPHICS:
            dropdown = self.selenium.find_element_by_link_text('Demographics')
            ActionChains(self.selenium).move_to_element(dropdown).perform()
            self.selenium.find_element_by_link_text(group).click()
            self.assertEqual(self.selenium.title, "Education: "+group)
        self.selenium.find_element_by_link_text('Home').click()

    def test_index_svg(self):
        """
        Make sure map of U.S. appears and is hoverable
        """
        map = self.selenium.find_element_by_id("graduation_rate_map")
        title = self.selenium.find_elements_by_class_name("graph-title")[0]
        self.assertEqual(title.text, "High School Graduation Rates for 2015-2016")
        washington = self.selenium.find_elements_by_class_name("Washington")[0]
        self.assertIn("rgb(247, 251, 255)",washington.get_attribute("style"))
        ActionChains(self.selenium).move_to_element(washington).perform()
        tooltip = self.selenium.find_elements_by_class_name("tooltip-label")[0]
        self.assertIn("Washington",tooltip.text)
        self.assertIn("60.0%",tooltip.text)
        washington = self.selenium.find_elements_by_class_name("Washington")[0]
        self.assertIn("rgb(255, 204, 102)",washington.get_attribute("style"))

    def test_states_links(self):
        """
        Make sure each link on the states page works
        """
        self.selenium.find_element_by_link_text('States').click()
        self.assertEqual(self.selenium.title, "Education: U.S. States")
        for state in STATES_LONG+["Bureau of Indian Affairs","District of Columbia"]:
            self.selenium.find_element_by_link_text(state).click()
            self.assertEqual(self.selenium.title, "Education: "+state)
            self.selenium.find_element_by_link_text('States').click()
        self.selenium.find_element_by_link_text('Home').click()

    def test_state_detail_links(self):
        """
        Make sure each demographic link on the state detail page works.
        """
        self.selenium.find_element_by_link_text('States').click()
        self.selenium.find_element_by_link_text('Alabama').click()
        for group in DEMOGRAPHICS:
            self.selenium.find_element_by_link_text(group).click()
            self.assertEqual(self.selenium.title, "Education: "+group)
            self.selenium.execute_script("window.history.go(-1)")
        self.selenium.find_element_by_link_text('Home').click()

    def test_state_detail_svg(self):
        """
        Make sure demographic grpah renders and is hoverable.
        """
        self.selenium.find_element_by_link_text('States').click()
        self.selenium.find_element_by_link_text('Alabama').click()
        self.selenium.find_element_by_id("statedemographics_svg")
        title = self.selenium.find_elements_by_class_name("graph-title")[0]
        self.assertEqual(title.text, "Percent of Alabama Cohort in Each Demographic")
        for group in DEMOGRAPHICS:
            bar = self.selenium.find_element_by_id(group.split()[0]+"-bar")
            self.assertIn("rgb(0, 0, 102)",bar.value_of_css_property("fill"))
            ActionChains(self.selenium).move_to_element(bar).perform()
            tooltip = self.selenium.find_elements_by_class_name("tooltip-label")[0]
            self.assertIn(group.split()[0],tooltip.text)
            self.assertIn("10.0%",tooltip.text)
            self.assertIn("rgb(255, 204, 102)",bar.value_of_css_property("fill"))
        self.selenium.find_element_by_link_text('Home').click()

    def test_demographics_links(self):
        """
        Make sure each link on the demographics page works.
        """
        self.selenium.find_element_by_link_text('Demographics').click()
        for group in DEMOGRAPHICS:
            self.selenium.find_element_by_link_text(group).click()
            self.assertEqual(self.selenium.title, "Education: "+group)
            self.selenium.execute_script("window.history.go(-1)")
        self.selenium.find_element_by_link_text('Home').click()

    def test_demographics_svg(self):
        """
        Make sure demographics graph renders and is hoverable
        """
        self.selenium.find_element_by_link_text('Demographics').click()
        self.selenium.find_element_by_id("demographics_svg")
        title = self.selenium.find_elements_by_class_name("graph-title")[0]
        self.assertEqual(title.text, "Percent of Cohort in Each Demographic")
        for group in DEMOGRAPHICS:
            bar = self.selenium.find_element_by_id(group.split()[0]+"-bar")
            self.assertIn("rgb(0, 0, 102)",bar.value_of_css_property("fill"))
            ActionChains(self.selenium).move_to_element(bar).perform()
            tooltip = self.selenium.find_elements_by_class_name("tooltip-label")[0]
            self.assertIn(group.split()[0],tooltip.text)
            if "English" in group:
                self.assertIn("7.7%",tooltip.text)
            else:
                self.assertIn("10.0%",tooltip.text)
            self.assertIn("rgb(255, 204, 102)",bar.value_of_css_property("fill"))
        self.selenium.find_element_by_link_text('Home').click()

    def test_demographics_detail_svg(self):
        """
        Make sure demographics detail pages graphs render and are hoverable
        """
        for group in DEMOGRAPHICS:
            self.selenium.find_element_by_link_text('Demographics').click()
            self.selenium.find_element_by_link_text(group).click()
            self.selenium.find_element_by_id("popsvg")
            title = self.selenium.find_elements_by_class_name("graph-title")[0]
            self.assertEqual(title.text, "Percent of Population that is {}".format(group))
            washington = self.selenium.find_elements_by_class_name("Washington")[0]
            if group == "English Learners":
                self.assertIn("gray",washington.get_attribute("style"))
            else:
                self.assertIn("rgb(8, 69, 148)",washington.get_attribute("style"))
                ActionChains(self.selenium).move_to_element(washington).perform()
                tooltip = self.selenium.find_elements_by_class_name("tooltip-label")[0]
                self.assertIn("Washington",tooltip.text)
                self.assertIn("10.0%",tooltip.text)
                washington = self.selenium.find_elements_by_class_name("Washington")[0]
                self.assertIn("rgb(255, 204, 102)",washington.get_attribute("style"))
            self.selenium.find_element_by_id("ratesvg")
            title = self.selenium.find_elements_by_class_name("graph-title")[1]
            self.assertEqual(title.text, "{} Graduation Rate".format(group))
            california = self.selenium.find_elements_by_class_name("California")[1]
            self.assertIn("rgb(8, 69, 148)",california.get_attribute("style"))
            ActionChains(self.selenium).move_to_element(california).perform()
            tooltip = self.selenium.find_elements_by_class_name("tooltip-label")[0]
            self.assertIn("California",tooltip.text)
            self.assertIn("90.0%",tooltip.text)
            california = self.selenium.find_elements_by_class_name("California")[1]
            self.assertIn("rgb(255, 204, 102)",california.get_attribute("style"))
        self.selenium.find_element_by_link_text('Home').click()
