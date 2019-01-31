from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, Max, Min, Count, Q, FloatField, F, OuterRef, Subquery
from django.db.models.functions import Cast
from .models import Team, Bracket, Tournament, Season_stats, Participant
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

def index(request):
	"""
	Main index page for the basketball project. The page displays the premise
	of the project as well as the family leaderboard.
	"""
	#total up how many touranment wins each person has and sort the list
	brackets = Bracket.objects.filter(name__in=["ME","MOM","AUNT"]).order_by('-year','-score').distinct('year')

	if brackets:
		wins = {}
		for b in brackets:
			wins[b.name] = wins.get(b.name, 0) + 1
		leaders = sorted(list(zip(wins.values(), wins.keys())), reverse=True)
		return render(request, 'basketball/index.html', {'leaders':leaders})
	else:
		return render(request, 'basketball/index.html')

def teams(request):
	"""
	The teams page contains a list of all NCAA division I mens basketball teams
	grouped by conference.
	"""

	data = []
	for (abbrev, full) in Team.CONFERENCE_NAMES:
		team_list = Team.objects.filter(conference=abbrev).order_by('school_name')
		if team_list:
			data.append((full, team_list))

	return render(request, 'basketball/teams.html', {'data': data})

def tournaments(request):
	"""
	The tournaments page lists links to each year of the tournament.
	"""
	winners = Season_stats.objects.filter(tournament_wins=6).order_by('-year')
	brackets = Bracket.objects.filter(name="TRUTH").order_by('-year')
	if not winners or not brackets or len(winners) != len(brackets):
		return render(request, 'basketball/tournaments.html')
	return render(request, 'basketball/tournaments.html', {'winners': zip(winners, brackets)})

def team_detail(request, team_id):
	"""
	The Team Detail page lists information for the team specified in the URL.
	Info includes tournament history, season stats, and location/venue.
	"""

	#make sure team_id is in the database
	try:
		team = Team.objects.get(pk=team_id)
	except ObjectDoesNotExist:
		message = "Team ID {} does not exist".format(team_id)
		return render(request, 'basketball/error.html', {"message": message})

	context = {}
	outcome = ["Made Round of 64","Made Round of 32","Made Sweet 16",
			"Made Elite Eight","Made Final Four","Made Championship","Won Championship"]
	agg_stats = team.season_stats_set.all().aggregate(
		Sum("tournament_wins"),Sum("tournament_losses"),
		Max("tournament_wins"),Min("tournament_seed"))
	context['wins'] = agg_stats["tournament_wins__sum"] if agg_stats["tournament_wins__sum"] else 0
	context['losses'] = agg_stats["tournament_losses__sum"] if agg_stats["tournament_losses__sum"] else 0
	context['seed'] = agg_stats["tournament_seed__min"] if agg_stats["tournament_seed__min"] else "N/A"
	if not agg_stats["tournament_seed__min"]:
		context["finish"] = "Did Not Make Tournament"
	else:
		context["finish"] = outcome[agg_stats["tournament_wins__max"]]

	#get season stats and dump ELO data into a JSON object to make a graph
	stats = team.season_stats_set.all().order_by('-year')
	elo_data = []
	for season in stats:
		elo_data.append({'year': season.year, 'elo': season.elo})
	json_data = json.dumps(elo_data)
	context['json_data'] = json_data
	context['team'] = team
	context['stats'] = stats
	context['first_year'] = elo_data[-1]["year"]
	return render(request, 'basketball/team_detail.html', context)

def tournament_detail(request, year):
	"""
	The tournament detail page lists the people who competed in that tournament
	and the score for their brackets. It also provides a link to the actual
	results of the tournament.
	"""
	brackets = Bracket.objects.filter(year=year).exclude(name='TRUTH').order_by('-score')
	actual = Bracket.objects.filter(year=year, name="TRUTH").get()
	upsets = actual.num_upsets()

	starting64 = Tournament.objects.filter(year=year).get()
	conferences = starting64.getConferences()
	elo_data = []
	conf_list = list(zip(conferences.values(),conferences.keys()))
	conf_list.sort(reverse=True)
	for f, c in conf_list:
		elo_data.append({'conference': c, 'frequency': f})
	json_data = json.dumps(elo_data)

	context = {'brackets': brackets, 'year':year, 'actual':actual,
		'upsets':upsets, "participants":["MOM","ME","AUNT"], 'json_data':json_data}
	return render(request, 'basketball/tournament_detail.html', context)

def bracket(request, bracket_id):
	"""
	The bracket page displays the picks that a person made for their bracket
	(or what actually happened if the true bracket is displayed).
	"""

	class Bracket_entry:
		"""
		The Bracket_entry class keeps track of the team id, their ELO rating
		for that season, and whether or not they won the game.
		"""
		def __init__(self, team, elo, correct=True):
			self.team = team
			self.elo = elo
			self.correct = correct

	#get the picks for the specified bracket and starting configuration of
	#tournament
	try:
		bracket = Bracket.objects.get(pk=bracket_id)
	except ObjectDoesNotExist:
		message = "Bracket ID {} does not exist".format(bracket_id)
		return render(request, 'basketball/error.html', {"message": message})
	starting64 = Tournament.objects.get(year=bracket.year)

	#get ELO information for each team
	ELO = Season_stats.objects.filter(year=bracket.year)
	ELO_dict = {}
	for row in ELO:
		ELO_dict[row.team] = row.elo

	#bundle information for each display
	context = {'bracket_name': bracket.name, 'bracket_year': bracket.year, 'bracket_score': bracket.score}
	context['top_left_1'] = Bracket_entry(starting64.top_left_1,ELO_dict[starting64.top_left_1])
	context['top_left_2'] = Bracket_entry(starting64.top_left_2,ELO_dict[starting64.top_left_2])
	context['top_left_3'] = Bracket_entry(starting64.top_left_3,ELO_dict[starting64.top_left_3])
	context['top_left_4'] = Bracket_entry(starting64.top_left_4,ELO_dict[starting64.top_left_4])
	context['top_left_5'] = Bracket_entry(starting64.top_left_5,ELO_dict[starting64.top_left_5])
	context['top_left_6'] = Bracket_entry(starting64.top_left_6,ELO_dict[starting64.top_left_6])
	context['top_left_7'] = Bracket_entry(starting64.top_left_7,ELO_dict[starting64.top_left_7])
	context['top_left_8'] = Bracket_entry(starting64.top_left_8,ELO_dict[starting64.top_left_8])
	context['top_left_9'] = Bracket_entry(starting64.top_left_9,ELO_dict[starting64.top_left_9])
	context['top_left_10'] = Bracket_entry(starting64.top_left_10,ELO_dict[starting64.top_left_10])
	context['top_left_11'] = Bracket_entry(starting64.top_left_11,ELO_dict[starting64.top_left_11])
	context['top_left_12'] = Bracket_entry(starting64.top_left_12,ELO_dict[starting64.top_left_12])
	context['top_left_13'] = Bracket_entry(starting64.top_left_13,ELO_dict[starting64.top_left_13])
	context['top_left_14'] = Bracket_entry(starting64.top_left_14,ELO_dict[starting64.top_left_14])
	context['top_left_15'] = Bracket_entry(starting64.top_left_15,ELO_dict[starting64.top_left_15])
	context['top_left_16'] = Bracket_entry(starting64.top_left_16,ELO_dict[starting64.top_left_16])
	context['bottom_left_1'] = Bracket_entry(starting64.bottom_left_1,ELO_dict[starting64.bottom_left_1])
	context['bottom_left_2'] = Bracket_entry(starting64.bottom_left_2,ELO_dict[starting64.bottom_left_2])
	context['bottom_left_3'] = Bracket_entry(starting64.bottom_left_3,ELO_dict[starting64.bottom_left_3])
	context['bottom_left_4'] = Bracket_entry(starting64.bottom_left_4,ELO_dict[starting64.bottom_left_4])
	context['bottom_left_5'] = Bracket_entry(starting64.bottom_left_5,ELO_dict[starting64.bottom_left_5])
	context['bottom_left_6'] = Bracket_entry(starting64.bottom_left_6,ELO_dict[starting64.bottom_left_6])
	context['bottom_left_7'] = Bracket_entry(starting64.bottom_left_7,ELO_dict[starting64.bottom_left_7])
	context['bottom_left_8'] = Bracket_entry(starting64.bottom_left_8,ELO_dict[starting64.bottom_left_8])
	context['bottom_left_9'] = Bracket_entry(starting64.bottom_left_9,ELO_dict[starting64.bottom_left_9])
	context['bottom_left_10'] = Bracket_entry(starting64.bottom_left_10,ELO_dict[starting64.bottom_left_10])
	context['bottom_left_11'] = Bracket_entry(starting64.bottom_left_11,ELO_dict[starting64.bottom_left_11])
	context['bottom_left_12'] = Bracket_entry(starting64.bottom_left_12,ELO_dict[starting64.bottom_left_12])
	context['bottom_left_13'] = Bracket_entry(starting64.bottom_left_13,ELO_dict[starting64.bottom_left_13])
	context['bottom_left_14'] = Bracket_entry(starting64.bottom_left_14,ELO_dict[starting64.bottom_left_14])
	context['bottom_left_15'] = Bracket_entry(starting64.bottom_left_15,ELO_dict[starting64.bottom_left_15])
	context['bottom_left_16'] = Bracket_entry(starting64.bottom_left_16,ELO_dict[starting64.bottom_left_16])
	context['top_right_1'] = Bracket_entry(starting64.top_right_1,ELO_dict[starting64.top_right_1])
	context['top_right_2'] = Bracket_entry(starting64.top_right_2,ELO_dict[starting64.top_right_2])
	context['top_right_3'] = Bracket_entry(starting64.top_right_3,ELO_dict[starting64.top_right_3])
	context['top_right_4'] = Bracket_entry(starting64.top_right_4,ELO_dict[starting64.top_right_4])
	context['top_right_5'] = Bracket_entry(starting64.top_right_5,ELO_dict[starting64.top_right_5])
	context['top_right_6'] = Bracket_entry(starting64.top_right_6,ELO_dict[starting64.top_right_6])
	context['top_right_7'] = Bracket_entry(starting64.top_right_7,ELO_dict[starting64.top_right_7])
	context['top_right_8'] = Bracket_entry(starting64.top_right_8,ELO_dict[starting64.top_right_8])
	context['top_right_9'] = Bracket_entry(starting64.top_right_9,ELO_dict[starting64.top_right_9])
	context['top_right_10'] = Bracket_entry(starting64.top_right_10,ELO_dict[starting64.top_right_10])
	context['top_right_11'] = Bracket_entry(starting64.top_right_11,ELO_dict[starting64.top_right_11])
	context['top_right_12'] = Bracket_entry(starting64.top_right_12,ELO_dict[starting64.top_right_12])
	context['top_right_13'] = Bracket_entry(starting64.top_right_13,ELO_dict[starting64.top_right_13])
	context['top_right_14'] = Bracket_entry(starting64.top_right_14,ELO_dict[starting64.top_right_14])
	context['top_right_15'] = Bracket_entry(starting64.top_right_15,ELO_dict[starting64.top_right_15])
	context['top_right_16'] = Bracket_entry(starting64.top_right_16,ELO_dict[starting64.top_right_16])
	context['bottom_right_1'] = Bracket_entry(starting64.bottom_right_1,ELO_dict[starting64.bottom_right_1])
	context['bottom_right_2'] = Bracket_entry(starting64.bottom_right_2,ELO_dict[starting64.bottom_right_2])
	context['bottom_right_3'] = Bracket_entry(starting64.bottom_right_3,ELO_dict[starting64.bottom_right_3])
	context['bottom_right_4'] = Bracket_entry(starting64.bottom_right_4,ELO_dict[starting64.bottom_right_4])
	context['bottom_right_5'] = Bracket_entry(starting64.bottom_right_5,ELO_dict[starting64.bottom_right_5])
	context['bottom_right_6'] = Bracket_entry(starting64.bottom_right_6,ELO_dict[starting64.bottom_right_6])
	context['bottom_right_7'] = Bracket_entry(starting64.bottom_right_7,ELO_dict[starting64.bottom_right_7])
	context['bottom_right_8'] = Bracket_entry(starting64.bottom_right_8,ELO_dict[starting64.bottom_right_8])
	context['bottom_right_9'] = Bracket_entry(starting64.bottom_right_9,ELO_dict[starting64.bottom_right_9])
	context['bottom_right_10'] = Bracket_entry(starting64.bottom_right_10,ELO_dict[starting64.bottom_right_10])
	context['bottom_right_11'] = Bracket_entry(starting64.bottom_right_11,ELO_dict[starting64.bottom_right_11])
	context['bottom_right_12'] = Bracket_entry(starting64.bottom_right_12,ELO_dict[starting64.bottom_right_12])
	context['bottom_right_13'] = Bracket_entry(starting64.bottom_right_13,ELO_dict[starting64.bottom_right_13])
	context['bottom_right_14'] = Bracket_entry(starting64.bottom_right_14,ELO_dict[starting64.bottom_right_14])
	context['bottom_right_15'] = Bracket_entry(starting64.bottom_right_15,ELO_dict[starting64.bottom_right_15])
	context['bottom_right_16'] = Bracket_entry(starting64.bottom_right_16,ELO_dict[starting64.bottom_right_16])
	context['top_left_r1_g1'] = Bracket_entry(bracket.top_left_r1_g1,ELO_dict[bracket.top_left_r1_g1],bracket.top_left_r1_g1_correct)
	context['top_left_r1_g2'] = Bracket_entry(bracket.top_left_r1_g2,ELO_dict[bracket.top_left_r1_g2],bracket.top_left_r1_g2_correct)
	context['top_left_r1_g3'] = Bracket_entry(bracket.top_left_r1_g3,ELO_dict[bracket.top_left_r1_g3],bracket.top_left_r1_g3_correct)
	context['top_left_r1_g4'] = Bracket_entry(bracket.top_left_r1_g4,ELO_dict[bracket.top_left_r1_g4],bracket.top_left_r1_g4_correct)
	context['top_left_r1_g5'] = Bracket_entry(bracket.top_left_r1_g5,ELO_dict[bracket.top_left_r1_g5],bracket.top_left_r1_g5_correct)
	context['top_left_r1_g6'] = Bracket_entry(bracket.top_left_r1_g6,ELO_dict[bracket.top_left_r1_g6],bracket.top_left_r1_g6_correct)
	context['top_left_r1_g7'] = Bracket_entry(bracket.top_left_r1_g7,ELO_dict[bracket.top_left_r1_g7],bracket.top_left_r1_g7_correct)
	context['top_left_r1_g8'] = Bracket_entry(bracket.top_left_r1_g8,ELO_dict[bracket.top_left_r1_g8],bracket.top_left_r1_g8_correct)
	context['bottom_left_r1_g1'] = Bracket_entry(bracket.bottom_left_r1_g1,ELO_dict[bracket.bottom_left_r1_g1],bracket.bottom_left_r1_g1_correct)
	context['bottom_left_r1_g2'] = Bracket_entry(bracket.bottom_left_r1_g2,ELO_dict[bracket.bottom_left_r1_g2],bracket.bottom_left_r1_g2_correct)
	context['bottom_left_r1_g3'] = Bracket_entry(bracket.bottom_left_r1_g3,ELO_dict[bracket.bottom_left_r1_g3],bracket.bottom_left_r1_g3_correct)
	context['bottom_left_r1_g4'] = Bracket_entry(bracket.bottom_left_r1_g4,ELO_dict[bracket.bottom_left_r1_g4],bracket.bottom_left_r1_g4_correct)
	context['bottom_left_r1_g5'] = Bracket_entry(bracket.bottom_left_r1_g5,ELO_dict[bracket.bottom_left_r1_g5],bracket.bottom_left_r1_g5_correct)
	context['bottom_left_r1_g6'] = Bracket_entry(bracket.bottom_left_r1_g6,ELO_dict[bracket.bottom_left_r1_g6],bracket.bottom_left_r1_g6_correct)
	context['bottom_left_r1_g7'] = Bracket_entry(bracket.bottom_left_r1_g7,ELO_dict[bracket.bottom_left_r1_g7],bracket.bottom_left_r1_g7_correct)
	context['bottom_left_r1_g8'] = Bracket_entry(bracket.bottom_left_r1_g8,ELO_dict[bracket.bottom_left_r1_g8],bracket.bottom_left_r1_g8_correct)
	context['top_right_r1_g1'] = Bracket_entry(bracket.top_right_r1_g1,ELO_dict[bracket.top_right_r1_g1],bracket.top_right_r1_g1_correct)
	context['top_right_r1_g2'] = Bracket_entry(bracket.top_right_r1_g2,ELO_dict[bracket.top_right_r1_g2],bracket.top_right_r1_g2_correct)
	context['top_right_r1_g3'] = Bracket_entry(bracket.top_right_r1_g3,ELO_dict[bracket.top_right_r1_g3],bracket.top_right_r1_g3_correct)
	context['top_right_r1_g4'] = Bracket_entry(bracket.top_right_r1_g4,ELO_dict[bracket.top_right_r1_g4],bracket.top_right_r1_g4_correct)
	context['top_right_r1_g5'] = Bracket_entry(bracket.top_right_r1_g5,ELO_dict[bracket.top_right_r1_g5],bracket.top_right_r1_g5_correct)
	context['top_right_r1_g6'] = Bracket_entry(bracket.top_right_r1_g6,ELO_dict[bracket.top_right_r1_g6],bracket.top_right_r1_g6_correct)
	context['top_right_r1_g7'] = Bracket_entry(bracket.top_right_r1_g7,ELO_dict[bracket.top_right_r1_g7],bracket.top_right_r1_g7_correct)
	context['top_right_r1_g8'] = Bracket_entry(bracket.top_right_r1_g8,ELO_dict[bracket.top_right_r1_g8],bracket.top_right_r1_g8_correct)
	context['bottom_right_r1_g1'] = Bracket_entry(bracket.bottom_right_r1_g1,ELO_dict[bracket.bottom_right_r1_g1],bracket.bottom_right_r1_g1_correct)
	context['bottom_right_r1_g2'] = Bracket_entry(bracket.bottom_right_r1_g2,ELO_dict[bracket.bottom_right_r1_g2],bracket.bottom_right_r1_g2_correct)
	context['bottom_right_r1_g3'] = Bracket_entry(bracket.bottom_right_r1_g3,ELO_dict[bracket.bottom_right_r1_g3],bracket.bottom_right_r1_g3_correct)
	context['bottom_right_r1_g4'] = Bracket_entry(bracket.bottom_right_r1_g4,ELO_dict[bracket.bottom_right_r1_g4],bracket.bottom_right_r1_g4_correct)
	context['bottom_right_r1_g5'] = Bracket_entry(bracket.bottom_right_r1_g5,ELO_dict[bracket.bottom_right_r1_g5],bracket.bottom_right_r1_g5_correct)
	context['bottom_right_r1_g6'] = Bracket_entry(bracket.bottom_right_r1_g6,ELO_dict[bracket.bottom_right_r1_g6],bracket.bottom_right_r1_g6_correct)
	context['bottom_right_r1_g7'] = Bracket_entry(bracket.bottom_right_r1_g7,ELO_dict[bracket.bottom_right_r1_g7],bracket.bottom_right_r1_g7_correct)
	context['bottom_right_r1_g8'] = Bracket_entry(bracket.bottom_right_r1_g8,ELO_dict[bracket.bottom_right_r1_g8],bracket.bottom_right_r1_g8_correct)
	context['top_left_r2_g1'] = Bracket_entry(bracket.top_left_r2_g1,ELO_dict[bracket.top_left_r2_g1],bracket.top_left_r2_g1_correct)
	context['top_left_r2_g2'] = Bracket_entry(bracket.top_left_r2_g2,ELO_dict[bracket.top_left_r2_g2],bracket.top_left_r2_g2_correct)
	context['top_left_r2_g3'] = Bracket_entry(bracket.top_left_r2_g3,ELO_dict[bracket.top_left_r2_g3],bracket.top_left_r2_g3_correct)
	context['top_left_r2_g4'] = Bracket_entry(bracket.top_left_r2_g4,ELO_dict[bracket.top_left_r2_g4],bracket.top_left_r2_g4_correct)
	context['bottom_left_r2_g1'] = Bracket_entry(bracket.bottom_left_r2_g1,ELO_dict[bracket.bottom_left_r2_g1],bracket.bottom_left_r2_g1_correct)
	context['bottom_left_r2_g2'] = Bracket_entry(bracket.bottom_left_r2_g2,ELO_dict[bracket.bottom_left_r2_g2],bracket.bottom_left_r2_g2_correct)
	context['bottom_left_r2_g3'] = Bracket_entry(bracket.bottom_left_r2_g3,ELO_dict[bracket.bottom_left_r2_g3],bracket.bottom_left_r2_g3_correct)
	context['bottom_left_r2_g4'] = Bracket_entry(bracket.bottom_left_r2_g4,ELO_dict[bracket.bottom_left_r2_g4],bracket.bottom_left_r2_g4_correct)
	context['top_right_r2_g1'] = Bracket_entry(bracket.top_right_r2_g1,ELO_dict[bracket.top_right_r2_g1],bracket.top_right_r2_g1_correct)
	context['top_right_r2_g2'] = Bracket_entry(bracket.top_right_r2_g2,ELO_dict[bracket.top_right_r2_g2],bracket.top_right_r2_g2_correct)
	context['top_right_r2_g3'] = Bracket_entry(bracket.top_right_r2_g3,ELO_dict[bracket.top_right_r2_g3],bracket.top_right_r2_g3_correct)
	context['top_right_r2_g4'] = Bracket_entry(bracket.top_right_r2_g4,ELO_dict[bracket.top_right_r2_g4],bracket.top_right_r2_g4_correct)
	context['bottom_right_r2_g1'] = Bracket_entry(bracket.bottom_right_r2_g1,ELO_dict[bracket.bottom_right_r2_g1],bracket.bottom_right_r2_g1_correct)
	context['bottom_right_r2_g2'] = Bracket_entry(bracket.bottom_right_r2_g2,ELO_dict[bracket.bottom_right_r2_g2],bracket.bottom_right_r2_g2_correct)
	context['bottom_right_r2_g3'] = Bracket_entry(bracket.bottom_right_r2_g3,ELO_dict[bracket.bottom_right_r2_g3],bracket.bottom_right_r2_g3_correct)
	context['bottom_right_r2_g4'] = Bracket_entry(bracket.bottom_right_r2_g4,ELO_dict[bracket.bottom_right_r2_g4],bracket.bottom_right_r2_g4_correct)
	context['top_left_ss_g1'] = Bracket_entry(bracket.top_left_ss_g1,ELO_dict[bracket.top_left_ss_g1],bracket.top_left_ss_g1_correct)
	context['top_left_ss_g2'] = Bracket_entry(bracket.top_left_ss_g2,ELO_dict[bracket.top_left_ss_g2],bracket.top_left_ss_g2_correct)
	context['bottom_left_ss_g1'] = Bracket_entry(bracket.bottom_left_ss_g1,ELO_dict[bracket.bottom_left_ss_g1],bracket.bottom_left_ss_g1_correct)
	context['bottom_left_ss_g2'] = Bracket_entry(bracket.bottom_left_ss_g2,ELO_dict[bracket.bottom_left_ss_g2],bracket.bottom_left_ss_g2_correct)
	context['top_right_ss_g1'] = Bracket_entry(bracket.top_right_ss_g1,ELO_dict[bracket.top_right_ss_g1],bracket.top_right_ss_g1_correct)
	context['top_right_ss_g2'] = Bracket_entry(bracket.top_right_ss_g2,ELO_dict[bracket.top_right_ss_g2],bracket.top_right_ss_g2_correct)
	context['bottom_right_ss_g1'] = Bracket_entry(bracket.bottom_right_ss_g1,ELO_dict[bracket.bottom_right_ss_g1],bracket.bottom_right_ss_g1_correct)
	context['bottom_right_ss_g2'] = Bracket_entry(bracket.bottom_right_ss_g2,ELO_dict[bracket.bottom_right_ss_g2],bracket.bottom_right_ss_g2_correct)
	context['top_left_ee'] = Bracket_entry(bracket.top_left_ee,ELO_dict[bracket.top_left_ee],bracket.top_left_ee_correct)
	context['bottom_left_ee'] = Bracket_entry(bracket.bottom_left_ee,ELO_dict[bracket.bottom_left_ee],bracket.bottom_left_ee_correct)
	context['top_right_ee'] = Bracket_entry(bracket.top_right_ee,ELO_dict[bracket.top_right_ee],bracket.top_right_ee_correct)
	context['bottom_right_ee'] = Bracket_entry(bracket.bottom_right_ee,ELO_dict[bracket.bottom_right_ee],bracket.bottom_right_ee_correct)
	context['ff_left'] = Bracket_entry(bracket.ff_left,ELO_dict[bracket.ff_left],bracket.ff_left_correct)
	context['ff_right'] = Bracket_entry(bracket.ff_right,ELO_dict[bracket.ff_right],bracket.ff_right_correct)
	context['championship'] = Bracket_entry(bracket.championship,ELO_dict[bracket.championship],bracket.championship_correct)

	return render(request, 'basketball/bracket.html', context)

def stats(request):
	#matchup_by_elo = Season_stats.objects.values(bin=(((F('tournament_lost_to__season_stats__elo')-F('elo'))/50*50)**2)**0.5) \
	#.exclude(tournament_lost_to__isnull = True) \
	#.annotate(wp=Cast(Count('pk',filter=Q(elo__gte=F('tournament_lost_to__season_stats__elo'))),FloatField())/Cast(Count('bin'),FloatField())) \
	#.order_by('-bin')
	test0 = Season_stats.objects.filter(team=OuterRef('tournament_lost_to'),year=OuterRef('year'))
	test1 = Season_stats.objects.exclude(tournament_lost_to__isnull=True) \
	.values(diff=(((Subquery(test0.values('elo'))-F('elo'))/50*50)**2)**0.5) \
	.annotate(wp=Cast(Count('pk',filter=Q(elo__lt=Subquery(test0.values('elo')))),FloatField())/Cast(Count('diff'),FloatField())) \
	.order_by('diff')

	matchup_by_elo = test1
	return render(request, 'basketball/stats.html', {'test':matchup_by_elo})

def participant(request,name):
	try:
		person = Participant.objects.get(name=name.upper())
	except Participant.DoesNotExist:
		message = "Participant {} does not exist".format(name)
		return render(request, 'basketball/error.html', {"message": message})

	context = {"person":person}
	context["json_finish_data"] = json.dumps([{"place":"1st","value":person.first_place},
		{"place":"2nd","value":person.second_place},{"place":"3rd","value":person.third_place}])
	return render(request, 'basketball/participant.html', context)

def stats_graph(request):
	graph = request.POST.get('graph', None)
	if graph == 'wp_by_elo':
		wp_by_elo = Season_stats.objects.values(bin=F('elo')/50*50) \
			.filter(made_tournament = True) \
			.annotate(wp=Cast(Sum('tournament_wins'),FloatField())/(Cast(Sum('tournament_wins'),FloatField())+Cast(Sum('tournament_losses'),FloatField()))*100) \
			.order_by('bin')
		data = {'wp':json.dumps(list(wp_by_elo), cls=DjangoJSONEncoder)}
	elif graph == 'wp_by_seed':
		wp_by_seed = Season_stats.objects.values(value=F("tournament_seed")) \
			.filter(made_tournament=True) \
			.annotate(wp=Cast(Sum('tournament_wins'),FloatField())/(Cast(Sum('tournament_wins'),FloatField())+Cast(Sum('tournament_losses'),FloatField()))*100) \
			.order_by('tournament_seed')
		data = {'wp':json.dumps(list(wp_by_seed), cls=DjangoJSONEncoder)}
	elif graph == 'wp_by_conference':
		wins = Cast(Sum('season_stats__tournament_wins', filter=Q(season_stats__made_tournament=True)), FloatField())
		losses = Cast(Sum('season_stats__tournament_losses', filter=Q(season_stats__made_tournament=True)), FloatField())
		wp_by_conference = Team.objects.values(value=F("conference")).annotate(wp=wins/(wins+losses)*100).order_by('-wp')
		data = {'wp': json.dumps(list(wp_by_conference), cls=DjangoJSONEncoder)}
	elif graph == 'wp_by_venue_capacity':
		wp_by_venue_capacity = Team.objects.values(bin=F('venue_capacity')/4000*4000) \
			.filter(season_stats__made_tournament = True) \
			.annotate(wp=Cast(Sum('season_stats__tournament_wins'),FloatField())/(Cast(Sum('season_stats__tournament_wins'),FloatField())+Cast(Sum('season_stats__tournament_losses'),FloatField()))*100) \
			.order_by('bin')
		data = {'wp':json.dumps(list(wp_by_venue_capacity), cls=DjangoJSONEncoder)}
	elif graph == 'wp_by_ppg':
		wp_by_ppg = Season_stats.objects.values(bin=F('ppg')-F('ppg')%4) \
			.filter(made_tournament = True) \
			.annotate(wp=Cast(Sum('tournament_wins'),FloatField())/(Cast(Sum('tournament_wins'),FloatField())+Cast(Sum('tournament_losses'),FloatField()))*100) \
			.order_by('bin')
		data = {'wp':json.dumps(list(wp_by_ppg), cls=DjangoJSONEncoder)}
	elif graph == 'wp_by_ppga':
		wp_by_ppga = Season_stats.objects.values(bin=F('ppga')-F('ppga')%4) \
			.filter(made_tournament = True) \
			.annotate(wp=Cast(Sum('tournament_wins'),FloatField())/(Cast(Sum('tournament_wins'),FloatField())+Cast(Sum('tournament_losses'),FloatField()))*100) \
			.order_by('bin')
		data = {'wp':json.dumps(list(wp_by_ppga), cls=DjangoJSONEncoder)}
	elif graph == 'wp_by_ppgd':
		wp_by_ppgd = Season_stats.objects.values(bin=(F('ppg')-F('ppga'))-(F('ppg')-F('ppga'))%2) \
			.filter(made_tournament = True) \
			.annotate(wp=Cast(Sum('tournament_wins'),FloatField())/(Cast(Sum('tournament_wins'),FloatField())+Cast(Sum('tournament_losses'),FloatField()))*100) \
			.order_by('bin')
		data = {'wp':json.dumps(list(wp_by_ppgd), cls=DjangoJSONEncoder)}
	elif graph == 'matchup_by_elo':
		lost_to = Season_stats.objects.filter(team=OuterRef('tournament_lost_to'),year=OuterRef('year'))
		matchup_by_elo = Season_stats.objects.exclude(tournament_lost_to__isnull=True) \
		.values(bin=(((Subquery(lost_to.values('elo'))-F('elo'))/50*50)**2)**0.5) \
		.annotate(wp=100*Cast(Count('pk',filter=Q(elo__gt=Subquery(lost_to.values('elo')))),FloatField())/Cast(Count('bin'),FloatField())) \
		.order_by('bin')
		data = {'wp':json.dumps(list(matchup_by_elo), cls=DjangoJSONEncoder)}
	elif graph == 'matchup_by_seed':
		lost_to = Season_stats.objects.filter(team=OuterRef('tournament_lost_to'),year=OuterRef('year'))
		matchup_by_seed = Season_stats.objects.exclude(tournament_lost_to__isnull=True) \
		.values(value=((Subquery(lost_to.values('tournament_seed'))-F('tournament_seed'))**2)**0.5) \
		.annotate(wp=100*Cast(Count('pk',filter=Q(tournament_seed__lt=Subquery(lost_to.values('tournament_seed')))),FloatField())/Cast(Count('value'),FloatField())) \
		.order_by('value')
		data = {'wp':json.dumps(list(matchup_by_seed), cls=DjangoJSONEncoder)}
	elif graph == 'matchup_by_ppg':
		lost_to = Season_stats.objects.filter(team=OuterRef('tournament_lost_to'),year=OuterRef('year'))
		matchup_by_ppg = Season_stats.objects.exclude(tournament_lost_to__isnull=True) \
		.values(bin=(((Subquery(lost_to.values('ppg'))-F('ppg'))-(Subquery(lost_to.values('ppg'))-F('ppg'))%2)**2)**0.5) \
		.annotate(wp=100*Cast(Count('pk',filter=Q(ppg__gt=Subquery(lost_to.values('ppg')))),FloatField())/Cast(Count('bin'),FloatField())) \
		.order_by('bin')
		data = {'wp':json.dumps(list(matchup_by_ppg), cls=DjangoJSONEncoder)}

	return JsonResponse(data)
