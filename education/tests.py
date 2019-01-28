from django.test import TestCase
from django.urls import reverse

from .models import State

STATES = ['AK','AL','AR','AZ','BI','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY']

def create_null_states():
    """
    Create data for the State database.
    """
    for s in STATES:
        State.objects.create(state=s,all_cohort=1,mam_cohort=0,mas_cohort=0,
        mbl_cohort=0,mhi_cohort=0,mtr_cohort=0,mwh_cohort=0,cwd_cohort=0,
        ecd_cohort=0,lep_cohort=0,num_schools=0,all_rate=0,mam_rate=None,
        mas_rate=None,mbl_rate=None,mhi_rate=None,mtr_rate=None,mwh_rate=None,
        cwd_rate=None,ecd_rate=None,lep_rate=None)

def create_states():
    """
    Create data for the State database.
    """
    for s in STATES:
        State.objects.create(state=s,all_cohort=1000,mam_cohort=100,mas_cohort=100,
        mbl_cohort=100,mhi_cohort=100,mtr_cohort=100,mwh_cohort=100,cwd_cohort=100,
        ecd_cohort=100,lep_cohort=100,num_schools=10,all_rate=0.9,mam_rate=0.9,
        mas_rate=0.9,mbl_rate=0.9,mhi_rate=0.9,mtr_rate=0.9,mwh_rate=0.9,
        cwd_rate=0.9,ecd_rate=0.9,lep_rate=0.9)

class EducationIndexViewTests(TestCase):
    def test_no_data(self):
        """
        If no data is in the database, no content is displayed but there is no
        map of graudation rates.
        """
        response = self.client.get(reverse('education:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get("json_data"), None)
        self.assertContains(response, "High School Graduation")
        self.assertContains(response, "How Rates Were Calculated")
        self.assertContains(response, "Home")
        self.assertNotContains(response, '<svg id="graduation_rate_map">')

    def test_with_data(self):
        """
        If state data is in the database, make sure the conents renders and a
        graph of the graudation rates is displayed.
        """
        create_states()
        response = self.client.get(reverse('education:index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context.get("json_data"), None)
        self.assertContains(response, "High School Graduation")
        self.assertContains(response, "How Rates Were Calculated")
        self.assertContains(response, '<svg id="graduation_rate_map">')

class EducationStatesViewTest(TestCase):

    def test_no_data(self):
        """
        Make sure the page renders and gives an error message if no data is available.
        """
        response = self.client.get(reverse('education:states'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get("states").count(), 0)
        self.assertContains(response, "No Data Available")
        self.assertNotContains(response, "Number of Public High Schools")

    def test_with_data(self):
        """
        Make sure page renders when state database is filled.
        """
        create_states()
        response = self.client.get(reverse('education:states'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get("states").count(), 52)
        self.assertContains(response, "Home")
        self.assertNotContains(response, "No Data Available")
        self.assertContains(response, "Number of Public High Schools")
        self.assertContains(response, "Mississippi")
        self.assertContains(response, "90.0%")
        self.assertContains(response, "1,000")
        self.assertContains(response, "10")

class EducationStateDetailsViewTest(TestCase):

    def test_no_data(self):
        """
        Make sure each state page renders if there is no database data.
        """
        for s in STATES:
            response = self.client.get(reverse('education:state_detail',args=(s,)))
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.context.get("message"), None)
            self.assertContains(response, "Error: No data for state {}".format(s))

    def test_with_null_data(self):
        """
        Make sure each state page renders if there is data in the database.
        """
        create_null_states()
        for s in STATES:
            response = self.client.get(reverse('education:state_detail',args=(s,)))
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.context.get("data"), None)
            self.assertNotEqual(response.context.get("json_data"), None)
            self.assertContains(response, "Students in 15-16 Cohort")
            self.assertNotContains(response, ">Native American</a></td>")

    def test_with_data(self):
        """
        Make sure each page renders if there is non-null data in the databasese
        """
        create_states()
        for s in STATES:
            response = self.client.get(reverse('education:state_detail',args=(s,)))
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.context.get("data"), None)
            self.assertNotEqual(response.context.get("json_data"), None)
            self.assertContains(response, "Students in 15-16 Cohort")
            self.assertContains(response, ">Native American</a></td>")

class EducationDemographicsViewTest(TestCase):

    def test_no_data(self):
        """
        Make sure demographics page renders even if there is no data in the
        database.
        """
        response = self.client.get(reverse('education:demographics'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get("json_data"), None)
        self.assertEqual(response.context.get("all_cohort"), None)
        self.assertEqual(response.context.get("all_rate"), None)
        for demo in State.GROUP_NAMES:
            self.assertEqual(response.context.get(demo+"_cohort"), None)
            self.assertEqual(response.context.get(demo+"_rate"), None)
        self.assertContains(response, "Home")
        self.assertContains(response, "No Data Available")
        self.assertNotContains(response, "Students in 15-16 Cohort")

    def test_with_data(self):
        """
        Make sure demographics page renders if there is data in the database.
        """
        create_states()
        response = self.client.get(reverse('education:demographics'))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context.get("json_data"), None)
        self.assertNotEqual(response.context.get("all_cohort"), None)
        self.assertNotEqual(response.context.get("all_rate"), None)
        for demo in State.GROUP_NAMES:
            self.assertNotEqual(response.context.get(demo+"_cohort"), None)
            self.assertNotEqual(response.context.get(demo+"_rate"), None)
        self.assertContains(response, "Home")
        self.assertContains(response, "Students in 15-16 Cohort")
        self.assertNotContains(response, "No Data Available")

class EducationDemographicDetailsViewTest(TestCase):

    def test_fake_group(self):
        """
        Make sure the page gives an error message if a group is specified that
        does not actually exist.
        """
        response = self.client.get(reverse('education:demographic_detail',args=("XYZ",)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home")
        self.assertContains(response, "Error: No such group XYZ")
        self.assertNotContains(response, '<svg id="popsvg">')

    def test_no_data(self):
        """
        Make sure all demographic pages render even when there is no data in the
        database.
        """
        for demo in State.GROUP_NAMES:
            response = self.client.get(reverse('education:demographic_detail',args=(demo,)))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Home")
            self.assertContains(response, "No Data Available")
            self.assertNotContains(response, '<svg id="popsvg">')

    def test_with_data(self):
        """
        """
        create_states()
        for demo in State.GROUP_NAMES:
            response = self.client.get(reverse('education:demographic_detail',args=(demo,)))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Home")
            self.assertNotContains(response, "No Data Available")
            self.assertContains(response, '<svg id="popsvg">')
