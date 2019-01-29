from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from .models import Team, Tournament, Bracket, Season_stats, Participant
from random import choice

def create_participants():
    """
    Create data for the State database.
    """
    Participant.objects.create(name="ME", first_place=1, second_place=2,
		third_place=3, correct_champions = 1, average_predicted_upsets = 14.4,
		average_correct_upsets=4.4)
    Participant.objects.create(name="MOM", first_place=2, second_place=3,
		third_place=1, correct_champions = 0, average_predicted_upsets = 18.4,
		average_correct_upsets=6.4)
    Participant.objects.create(name="AUNT", first_place=3, second_place=1,
		third_place=2, correct_champions = 2, average_predicted_upsets = 11.4,
		average_correct_upsets=5.4)

def create_teams():
	"""
	Create a set of fake 64 college basketball teams.
	"""
	for i in range(64):
		n = str(i)
		Team.objects.create(school_name="Team"+n,school_alias="T"+n,school_mascot="M"+n,
		conference=choice(Team.CONFERENCE_NAMES)[0],venue_city="C"+n,venue_state=choice(Team.STATE_NAMES)[0],
		venue_name="N"+n,venue_capacity=i*10)

def create_tournaments():
    """
    Create a Tournament with the four provided regions in the given year using the first 64 teams teams
    in alphabetical order.
    """
    team_list = Team.objects.order_by('school_name')
    for year in range(2006,2019):
        Tournament.objects.create(year=str(year), top_left_region="EAST", bottom_left_region="MIDWEST", top_right_region="SOUTH", bottom_right_region="WEST",
        top_left_1=team_list[0],top_left_2=team_list[1],top_left_3=team_list[2],top_left_4=team_list[3],
        top_left_5=team_list[4],top_left_6=team_list[5],top_left_7=team_list[6],top_left_8=team_list[7],
        top_left_9=team_list[8],top_left_10=team_list[9],top_left_11=team_list[10],top_left_12=team_list[11],
        top_left_13=team_list[12],top_left_14=team_list[13],top_left_15=team_list[14],top_left_16=team_list[15],
        bottom_left_1=team_list[16],bottom_left_2=team_list[17],bottom_left_3=team_list[18],bottom_left_4=team_list[19],
        bottom_left_5=team_list[20],bottom_left_6=team_list[21],bottom_left_7=team_list[22],bottom_left_8=team_list[23],
        bottom_left_9=team_list[24],bottom_left_10=team_list[25],bottom_left_11=team_list[26],bottom_left_12=team_list[27],
        bottom_left_13=team_list[28],bottom_left_14=team_list[29],bottom_left_15=team_list[30],bottom_left_16=team_list[31],
        top_right_1=team_list[32],top_right_2=team_list[33],top_right_3=team_list[34],top_right_4=team_list[35],
        top_right_5=team_list[36],top_right_6=team_list[37],top_right_7=team_list[38],top_right_8=team_list[39],
        top_right_9=team_list[40],top_right_10=team_list[41],top_right_11=team_list[42],top_right_12=team_list[43],
        top_right_13=team_list[44],top_right_14=team_list[45],top_right_15=team_list[46],top_right_16=team_list[47],
        bottom_right_1=team_list[48],bottom_right_2=team_list[49],bottom_right_3=team_list[50],bottom_right_4=team_list[51],
        bottom_right_5=team_list[52],bottom_right_6=team_list[53],bottom_right_7=team_list[54],bottom_right_8=team_list[55],
        bottom_right_9=team_list[56],bottom_right_10=team_list[57],bottom_right_11=team_list[58],bottom_right_12=team_list[59],
        bottom_right_13=team_list[60],bottom_right_14=team_list[61],bottom_right_15=team_list[62],bottom_right_16=team_list[63])

def create_brackets():
    for year in range(2006,2019):
        create_bracket("TRUTH",str(year))
        create_bracket("ME",str(year))
        create_bracket("MOM",str(year))
        create_bracket("AUNT",str(year))

def create_bracket(name, year):
	"""
	Create a fake bracket with given name and year.
	"""
	seeds = Tournament.objects.get(year=year)
	return Bracket.objects.create(name=name, year=year, top_left_r1_g1=seeds.top_left_1, top_left_r1_g2=seeds.top_left_8,
	top_left_r1_g3=seeds.top_left_5, top_left_r1_g4=seeds.top_left_4, top_left_r1_g5=seeds.top_left_6,
	top_left_r1_g6=seeds.top_left_3, top_left_r1_g7=seeds.top_left_7, top_left_r1_g8=seeds.top_left_2,
	bottom_left_r1_g1=seeds.bottom_left_1, bottom_left_r1_g2=seeds.bottom_left_8,
	bottom_left_r1_g3=seeds.bottom_left_5, bottom_left_r1_g4=seeds.bottom_left_4, bottom_left_r1_g5=seeds.bottom_left_6,
	bottom_left_r1_g6=seeds.bottom_left_3, bottom_left_r1_g7=seeds.bottom_left_7, bottom_left_r1_g8=seeds.bottom_left_2,
	top_right_r1_g1=seeds.top_right_1, top_right_r1_g2=seeds.top_right_8,
	top_right_r1_g3=seeds.top_right_5, top_right_r1_g4=seeds.top_right_4, top_right_r1_g5=seeds.top_right_6,
	top_right_r1_g6=seeds.top_right_3, top_right_r1_g7=seeds.top_right_7, top_right_r1_g8=seeds.top_right_2,
	bottom_right_r1_g1=seeds.bottom_right_1, bottom_right_r1_g2=seeds.bottom_right_8,
	bottom_right_r1_g3=seeds.bottom_right_5, bottom_right_r1_g4=seeds.bottom_right_4, bottom_right_r1_g5=seeds.bottom_right_6,
	bottom_right_r1_g6=seeds.bottom_right_3, bottom_right_r1_g7=seeds.bottom_right_7, bottom_right_r1_g8=seeds.bottom_right_2,
	top_left_r2_g1=seeds.top_left_1, top_left_r2_g2=seeds.top_left_4,top_left_r2_g3=seeds.top_left_3, top_left_r2_g4=seeds.top_left_2,
	bottom_left_r2_g1=seeds.bottom_left_1, bottom_left_r2_g2=seeds.bottom_left_4,bottom_left_r2_g3=seeds.bottom_left_3, bottom_left_r2_g4=seeds.bottom_left_2,
	top_right_r2_g1=seeds.top_right_1, top_right_r2_g2=seeds.top_right_4,top_right_r2_g3=seeds.top_right_3, top_right_r2_g4=seeds.top_right_2,
	bottom_right_r2_g1=seeds.bottom_right_1, bottom_right_r2_g2=seeds.bottom_right_4,bottom_right_r2_g3=seeds.bottom_right_3, bottom_right_r2_g4=seeds.bottom_right_2,\
	top_left_ss_g1=seeds.top_left_1, top_left_ss_g2=seeds.top_left_2,bottom_left_ss_g1=seeds.bottom_left_1, bottom_left_ss_g2=seeds.bottom_left_2,
	top_right_ss_g1=seeds.top_right_1, top_right_ss_g2=seeds.top_right_2,bottom_right_ss_g1=seeds.bottom_right_1, bottom_right_ss_g2=seeds.bottom_right_2,
	top_left_ee=seeds.top_left_1, bottom_left_ee=seeds.bottom_left_1, top_right_ee=seeds.top_right_1, bottom_right_ee=seeds.bottom_right_1,
	ff_left=seeds.top_left_1,ff_right=seeds.top_right_1,championship=seeds.top_left_1)

def create_stats():
    """
    Create season stats for the given year for all teams in the database.
    """
    team_list = Team.objects.order_by('school_name')
    for team in team_list:
        for year in range(2006,2019):
            Season_stats.objects.create(team=team, year=str(year), elo=1700, wins=22, losses=2,
            ppg=88.1, ppga=64.6, made_tournament=True, tournament_seed=1,
            tournament_wins=6,tournament_losses=0,
            tournament_region=None,tournament_lost_to=None)

class SeleniumBasketballTests(LiveServerTestCase):

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
        create_participants()
        create_teams()
        create_tournaments()
        create_brackets()
        create_stats()
        self.selenium.get('{}{}'.format(self.live_server_url, '/basketball'))

    def test_navbar_links(self):
        """
        Make sure all links in navbar open correctly
        """
        self.selenium.find_elements_by_class_name("navbar-brand")[0].click()
        self.assertEqual(self.selenium.title, "Smeds Project Page")
        self.selenium.find_element_by_link_text('Basketball Project').click()
        self.assertEqual(self.selenium.title, "Basketball Project")
        self.selenium.find_element_by_link_text('Tournaments').click()
        self.assertEqual(self.selenium.title, "Basketball: Tournaments")
        self.selenium.find_element_by_link_text('Teams').click()
        self.assertEqual(self.selenium.title, "Basketball: Teams")
        self.selenium.find_element_by_link_text('Explore the Data').click()
        self.assertEqual(self.selenium.title, "Basketball: Stats Explorer")
        self.selenium.find_element_by_link_text('Home').click()
        self.assertEqual(self.selenium.title, "Basketball Project")
        for year in range(2006,2019):
            dropdown = self.selenium.find_element_by_link_text('Tournaments')
            ActionChains(self.selenium).move_to_element(dropdown).perform()
            self.selenium.find_element_by_link_text(str(year)).click()
            self.assertEqual(self.selenium.title, "Basketball: "+str(year)+" Tournament")
        self.selenium.find_element_by_link_text('Home').click()

    def test_index_links(self):
        """
        Make sure all links on index page open correctly
        """
        self.selenium.find_element_by_link_text("Wikipedia").click()
        WebDriverWait(self.selenium, 10).until(EC.number_of_windows_to_be(2))
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        self.assertEqual(self.selenium.title, "Elo rating system - Wikipedia")
        self.selenium.close()
        self.selenium.switch_to_window(self.selenium.window_handles[0])
        for participant in ["Mom","Aunt","Me"]:
            self.selenium.find_element_by_link_text(participant).click()
            self.assertEqual(self.selenium.title, "Basketball: "+participant)
            self.selenium.find_element_by_link_text("Home").click()
