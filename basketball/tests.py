from django.test import TestCase
from django.urls import reverse

from .models import Team, Tournament, Bracket, Season_stats, Participant
from random import choice

def create_teams():
	"""
	Create a set of fake 64 college basketball teams.
	"""
	for i in range(64):
		n = str(i)
		Team.objects.create(school_name="Team"+n,school_alias="T"+n,school_mascot="M"+n,
		conference=choice(Team.CONFERENCE_NAMES)[0],venue_city="C"+n,venue_state=choice(Team.STATE_NAMES)[0],
		venue_name="N"+n,venue_capacity=i*10)

def create_stats(year):
	"""
	Create season stats for the given year for all teams in the database.
	"""
	team_list = Team.objects.order_by('school_name')
	for team in team_list:
		if team.school_name != "Team0":
			Season_stats.objects.create(team=team, year=year, elo=1500, wins=12, losses=5,
			ppg=80.1, ppga=74.6, made_tournament=False, tournament_seed=None,
			tournament_wins=None,tournament_losses=None,
			tournament_region=None,tournament_lost_to=None)
		else:
			Season_stats.objects.create(team=team, year=year, elo=1700, wins=22, losses=2,
			ppg=88.1, ppga=64.6, made_tournament=True, tournament_seed=1,
			tournament_wins=6,tournament_losses=0,
			tournament_region=None,tournament_lost_to=None)

def create_tournament(r1,r2,r3,r4,year):
	"""
	Create a Tournament with the four provided regions in the given year using the first 64 teams teams
	in alphabetical order.
	"""
	team_list = Team.objects.order_by('school_name')
	return Tournament.objects.create(year=year, top_left_region=r1, bottom_left_region=r2, top_right_region=r3, bottom_right_region=r4,
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

def create_participant(name):
	"""
	Create a fake bracket with the given name
	"""
	return Participant.objects.create(name=name, first_place=1, second_place=2,
		third_place=3, correct_champions = 0, average_predicted_upsets = 14.4,
		average_correct_upsets=4.4)

class BasketballIndexViewTests(TestCase):
	def test_no_data(self):
		"""
		If no tournaments are in the database, no leaderboard is displayed on the main page.
		"""
		response = self.client.get(reverse('basketball:index'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context.get("leaders"), None)
		self.assertContains(response, "March Madness Sadness")
		self.assertContains(response, "ELO Ratings")
		self.assertContains(response, "Explore the Data")
		self.assertNotContains(response, "Tournament Wins Since 2006")

	def test_tournament_data(self):
		"""
		If at least one bracket for me/mom/aunt is in the database, the main
		page is correctly rendered with a leaderboard.
		"""
		create_teams()
		create_tournament("east","west","south","midwest",2013)
		create_bracket("TRUTH",2013)
		create_bracket("ME",2013)
		response = self.client.get(reverse('basketball:index'))
		self.assertEqual(len(response.context.get("leaders")), 1)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "March Madness Sadness")
		self.assertContains(response, "ELO Ratings")
		self.assertContains(response, "Explore the Data")
		self.assertContains(response, "Tournament Wins Since 2006")

class TournamentViewTests(TestCase):

	def test_no_data(self):
		"""
		Make sure page renders even if no data is in the database.
		"""
		response = self.client.get(reverse('basketball:tournaments'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Explore the Data")
		self.assertContains(response, "No tournament data available")
		self.assertNotContains(response, "ELO Rating")

	def test_with_data(self):
		"""
		Make sure page renders if there is a team that won a tournament
		"""
		create_teams()
		create_tournament("east","west","south","midwest",2013)
		create_bracket("TRUTH",2013)
		create_stats(2013)
		response = self.client.get(reverse('basketball:tournaments'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Explore the Data")
		self.assertContains(response, "ELO Rating")
		self.assertNotContains(response, "No tournament data available")

class TeamViewTests(TestCase):

	def test_no_data(self):
		"""
		Make sure page renders even if there is no data in the database
		"""
		response = self.client.get(reverse('basketball:teams'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Explore the Data")
		self.assertContains(response, "No teams available")
		self.assertNotContains(response, "Team13")

	def test_with_data(self):
		"""
		Make sure page renders if there are teams in the database table
		"""
		create_teams()
		response = self.client.get(reverse('basketball:teams'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Explore the Data")
		self.assertContains(response, "Team13")
		self.assertNotContains(response, "No teams available")

class ParticipantViewTests(TestCase):

	def test_no_data(self):
		"""
		Make sure page renders even if invalid participant name is requested
		"""
		response = self.client.get(reverse('basketball:participant',args=("XYZ",)))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context.get("person"), None)
		self.assertNotEqual(response.context.get("message"), None)
		self.assertContains(response, "Explore the Data")
		self.assertContains(response, "Participant XYZ does not exist")
		self.assertNotContains(response, "First Place Finishes")

	def test_with_data(self):
		"""
		Make sure all participant pages render
		"""
		for (p,_) in Participant.PARTICIPANT_NAMES:
			participant = create_participant(p)
			response = self.client.get(reverse('basketball:participant',args=(p,)))
			self.assertEqual(response.status_code, 200)
			self.assertEqual(response.context.get("person"), participant)
			self.assertNotEqual(response.context.get("json_finish_data"), None)
			self.assertContains(response, "Explore the Data")
			self.assertContains(response, "First Place Finishes")
			self.assertNotContains(response, "does not exist")
