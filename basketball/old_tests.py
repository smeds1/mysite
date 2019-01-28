from django.test import TestCase
from django.urls import reverse

from .models import Team, Tournament, Bracket, Season_stats
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
		Season_stats.objects.create(team=team, year=year, elo=1500, wins=12, losses=5,
		ppg=80.1, ppa=74.6, made_tournament=False, tournament_seed="Null",
		tournament_wins="Null",tournament_losses="Null",
		tournament_region="Null",tournament_lost_to=Null)

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

class TeamModelTests(TestCase):

	def test_large_market(self):
		"""
		test to see if a large market team is correctly identified
		"""
		fake_team = Team(venue_capacity=10000)
		self.assertIs(fake_team.market_size(), "Large")

	def test_medium_market(self):
		"""
		test to see if a medium market team is correctly identified
		"""
		fake_team = Team(venue_capacity=6000)
		self.assertIs(fake_team.market_size(), "Medium")

	def test_small_market(self):
		"""
		test to see if a small market team is correctly identified
		"""
		fake_team = Team(venue_capacity=2000)
		self.assertIs(fake_team.market_size(), "Small")

class BasketballIndexViewTests(TestCase):
	def test_no_data(self):
		"""
		If no tournaments are in the database, no leaderboard is displayed on the main page.
		"""
		response = self.client.get(reverse('basketball:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "March Madness Sadness")
		self.assertNotContains(response, "All Time Leaderboard")

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
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "March Madness Sadness")
		self.assertContains(response, "All Time Leaderboard")

class BasketballTeamsViewTests(TestCase):
	def test_no_teams(self):
		"""
		If no teams are in the database, an appropriate message is displayed
		"""
		response = self.client.get(reverse('basketball:teams'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No teams available")

	def test_team_data(self):
		"""
		If team data is available, the teams page is correctly rendered.
		"""
		create_teams()
		response = self.client.get(reverse('basketball:teams'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Team1")

class BasketballTeamDetailViewTests(TestCase):
	def test_not_found(self):
		"""
		If the team_id is not found in the database, display an error message.
		"""
		response = self.client.get(reverse('basketball:team_detail',args=(1,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Error: Team ID 1 does not exist")

	def test_no_stats(self):
		"""
		If a team is in the database, but there are no season stats, omit the
		historical stats section
		"""
		fake_team = Team.objects.create(school_name="Team",school_alias="T",school_mascot="Mascot",
			conference=choice(Team.CONFERENCE_NAMES)[0],venue_city="C",venue_state=choice(Team.STATE_NAMES)[0],
			venue_name="N",venue_capacity=10000)
		response = self.client.get(reverse('basketball:team_detail',args=(fake_team.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Team Mascot")
		self.assertContains(response, "Venue Capacity")
		self.assertNotContains(response, "Tournament Record")
		self.assertNotContains(response, "Historical Stats")

	def test_valid_team(self):
		"""
		If the team_id is found in the database, display the page.
		"""
		fake_team = Team.objects.create(school_name="Team",school_alias="T",school_mascot="Mascot",
			conference=choice(Team.CONFERENCE_NAMES)[0],venue_city="C",venue_state=choice(Team.STATE_NAMES)[0],
			venue_name="N",venue_capacity=10000)
		create_stats(2018)
		response = self.client.get(reverse('basketball:team_detail',args=(fake_team.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Team Mascot")
		self.assertContains(response, "Historical Stats")
"""
class BasketballTournamentsViewTests(TestCase):
	def test_no_tournaments(self):
		"""
		If no tournament data is available, display an appropriate message.
		"""
		response = self.client.get(reverse('basketball:tournaments'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No data available")

	def test_no_leaderboard(self):
		"""
		If not historical bracket data is available, do not display the leaderboard.
		"""
		response = self.client.get(reverse('basketball:tournaments'))
		self.assertEqual(response.status_code, 200)
		self.assertNotContains(response, "All Time Leaderboard")

	def test_with_data(self):
		"""
		If tournaments and brackets exist in the database, render an appropriate page.
		"""
		create_teams()
		create_tournament("east","west","south","midwest",2013)
		create_bracket("TRUTH",2013)
		create_bracket("test bracket",2013)
		response = self.client.get(reverse('basketball:tournaments'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "2013 Season")
		self.assertContains(response, "All Time Leaderboard")

class BasketballTournamentDetailsViewTests(TestCase):
	def test_no_tournament(self):
		"""
		If no tournament has been entered for the given year, display an appropriate message.
		"""
		response = self.client.get(reverse('basketball:tournament_detail',args=(2013,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No tournament data available for 2013.")

	def test_no_brackets(self):
		"""
		If there are no brackets in the database, do not display a leaderboard.
		"""
		create_teams()
		create_tournament("east","west","south","midwest",2013)
		create_bracket("TRUTH",2013)
		response = self.client.get(reverse('basketball:tournament_detail',args=(2013,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "2013 Final Results")
		self.assertNotContains(response, "Final Standings")

	def test_has_brackets(self):
		"""
		If there are brackets in the database, make sure a leaderboard is displayed.
		"""
		create_teams()
		create_tournament("east","west","south","midwest",2013)
		create_bracket("TRUTH",2013)
		create_bracket("Test",2013)
		response = self.client.get(reverse('basketball:tournament_detail',args=(2013,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "2013 Final Results")
		self.assertContains(response, "Final Standings")

class BasketballBracketViewTests(TestCase):
	def test_no_data(self):
		"""
		If the bracket_id in the URL does not exist, render a 404 not found.
		"""
		response = self.client.get(reverse('basketball:bracket',args=(1,)))
		self.assertEqual(response.status_code, 404)

	def test_has_data(self):
		"""
		If a bracket does exist, render the correct page.
		"""
		create_teams()
		create_stats(2018)
		create_tournament("east","west","south","midwest",2018)
		create_bracket("TRUTH",2018)
		test_bracket = create_bracket("Test",2018)
		response = self.client.get(reverse('basketball:bracket',args=(test_bracket.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, test_bracket.name)
		self.assertContains(response, test_bracket.score)
		self.assertContains(response, test_bracket.championship)
"""
