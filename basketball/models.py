from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Team(models.Model):
	"""
	Class to represent and NCAA Division I basketball Team.
	"""

	#conference abbreviations
	AE = 'AE'
	AAC = 'AAC'
	A10 = 'A10'
	ACC = 'ACC'
	AS = 'AS'
	BIG12 = 'BIG12'
	BIGEAST = 'BIGEAST'
	BIGSKY = 'BIGSKY'
	BIGSOUTH = 'BIGSOUTH'
	BIG10 = 'BIG10'
	BIGWEST = 'BIGWEST'
	COLONIAL = 'COLONIAL'
	CUSA = 'CUSA'
	HORIZON = 'HORIZON'
	IVY = 'IVY'
	MAAC = 'MAAC'
	MEAC = 'MEAC'
	MAC = 'MAC'
	MVC = 'MVC'
	MWC = 'MWC'
	NEAST = 'NE'
	OVC = 'OVC'
	PAC12 = 'PAC12'
	PATRIOT = 'PATRIOT'
	SEC = 'SEC'
	SOUTHERN = 'SOUTHERN'
	SOUTHLAND = 'SOUTHLAND'
	SWAC = 'SWAC'
	SUMMIT = 'SUMMIT'
	SUNBELT = 'SUNBELT'
	WCC = 'WCC'
	WAC = 'WAC'

	#conference names
	CONFERENCE_NAMES = (
        (AE, 'America East'),
		(AAC, 'American Athletic'),
		(A10, 'Atlantic 10'),
		(ACC, 'Atlantic Coast'),
		(AS, 'Atlantic Sun'),
		(BIG12, 'Big 12'),
		(BIGEAST, 'Big East'),
		(BIGSKY, 'Big Sky'),
		(BIGSOUTH, 'Big South'),
		(BIG10, 'Big Ten'),
		(BIGWEST, 'Big West'),
		(COLONIAL, 'Colonial'),
		(CUSA, 'Conference USA'),
		(HORIZON, 'Horizon'),
		(IVY, 'Ivy'),
		(MAAC, 'Metro Atlantic Athletic'),
		(MEAC, 'Mid Eastern Athletic'),
		(MAC, 'Mid-American'),
		(MVC, 'Missouri Valley'),
		(MWC, 'Mountain West'),
		(NEAST, 'Northeast'),
		(OVC, 'Ohio Valley'),
		(PAC12, 'Pacific 12'),
		(PATRIOT, 'Patriot League'),
		(SEC, 'Southeastern'),
		(SOUTHERN, 'Southern'),
		(SOUTHLAND, 'Southland'),
		(SWAC, 'Southwestern Athletic'),
		(SUMMIT, 'Summit League'),
		(SUNBELT, 'Sun Belt'),
		(WCC, 'West Coast'),
		(WAC, 'Western Athletic'),
    )

	#U.S. state abbreviations
	AL = 'AL'
	AR = 'AR'
	AZ = 'AZ'
	CA = 'CA'
	CO = 'CO'
	CT = 'CT'
	DC = 'DC'
	DE = 'DE'
	FL = 'FL'
	GA = 'GA'
	HI = 'HI'
	IA = 'IA'
	ID = 'ID'
	IL = 'IL'
	IN = 'IN'
	KS = 'KS'
	KY = 'KY'
	LA = 'LA'
	MA = 'MA'
	MD = 'MD'
	ME = 'ME'
	MI = 'MI'
	MN = 'MN'
	MO = 'MO'
	MS = 'MS'
	MT = 'MT'
	NC = 'NC'
	ND = 'ND'
	NE = 'NE'
	NH = 'NH'
	NJ = 'NJ'
	NM = 'NM'
	NV = 'NV'
	NY = 'NY'
	OH = 'OH'
	OK = 'OK'
	OR = 'OR'
	PA = 'PA'
	RI = 'RI'
	SC = 'SC'
	SD = 'SD'
	TN = 'TN'
	TX = 'TX'
	UT = 'UT'
	VA = 'VA'
	VT = 'VT'
	WA = 'WA'
	WI = 'WI'
	WV = 'WV'
	WY = 'WY'

	STATE_NAMES = (
		(AL, 'AL'),
		(AR, 'AR'),
		(AZ, 'AZ'),
		(CA, 'CA'),
		(CO, 'CO'),
		(CT, 'CT'),
		(DC, 'DC'),
		(DE, 'DE'),
		(FL, 'FL'),
		(GA, 'GA'),
		(HI, 'HI'),
		(IA, 'IA'),
		(ID, 'ID'),
		(IL, 'IL'),
		(IN, 'IN'),
		(KS, 'KS'),
		(KY, 'KY'),
		(LA, 'LA'),
		(MA, 'MA'),
		(MD, 'MD'),
		(ME, 'ME'),
		(MI, 'MI'),
		(MN, 'MN'),
		(MO, 'MO'),
		(MS, 'MS'),
		(MT, 'MT'),
		(NC, 'NC'),
		(ND, 'ND'),
		(NE, 'NE'),
		(NH, 'NH'),
		(NJ, 'NJ'),
		(NM, 'NM'),
		(NV, 'NV'),
		(NY, 'NY'),
		(OH, 'OH'),
		(OK, 'OK'),
		(OR, 'OR'),
		(PA, 'PA'),
		(RI, 'RI'),
		(SC, 'SC'),
		(SD, 'SD'),
		(TN, 'TN'),
		(TX, 'TX'),
		(UT, 'UT'),
		(VA, 'VA'),
		(VT, 'VT'),
		(WA, 'WA'),
		(WI, 'WI'),
		(WV, 'WV'),
		(WY, 'WY'),
    )

	#fields in the database table
	school_name = models.CharField(max_length=50, unique=True)
	school_alias = models.CharField(max_length=5)
	school_mascot = models.CharField(max_length=50)
	conference = models.CharField(max_length=10,choices=CONFERENCE_NAMES)
	venue_city = models.CharField(max_length=20)
	venue_state = models.CharField(max_length=2,choices=STATE_NAMES)
	venue_name = models.CharField(max_length=60)
	venue_capacity = models.IntegerField(validators=[MinValueValidator(1)])

	def __str__(self):
		"""
		Print out the school's full name when a team is printed.
		"""
		return self.school_name

	def market_size(self):
		"""
		Return if a school is considered large (>10,000), medium (5000-10,000),
		or small (<5000).
		"""
		if self.venue_capacity < 5000:
			return "Small"
		elif self.venue_capacity < 10000:
			return "Medium"
		else:
			return "Large"

		""" Messed up an aggretate query
		class Meta:
		"""
		#Order schools alphabetically by name when listing.
		"""
		ordering = ["school_name"]
		"""

class Bracket(models.Model):
	"""
	Class to represent a bracket of the NCAA Mens March Madness Tournamentself.
	A bracket can represent what actually happened in each game or someone's
	predictions of what will happen in the future for a given tournament.
	"""

	#database fields
	name = models.CharField(max_length=50)
	year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1939)],default=datetime.date.today().year)
	score = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),MaxValueValidator(192)])
	top_left_r1_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r1_g1_id',verbose_name="Top Left Round 1 Game 1 Winner")
	top_left_r1_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r1_g2_id',verbose_name="Top Left Round 1 Game 2 Winner")
	top_left_r1_g3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r1_g3_id',verbose_name="Top Left Round 1 Game 3 Winner")
	top_left_r1_g4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r1_g4_id',verbose_name="Top Left Round 1 Game 4 Winner")
	top_left_r1_g5 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r1_g5_id',verbose_name="Top Left Round 1 Game 5 Winner")
	top_left_r1_g6 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r1_g6_id',verbose_name="Top Left Round 1 Game 6 Winner")
	top_left_r1_g7 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r1_g7_id',verbose_name="Top Left Round 1 Game 7 Winner")
	top_left_r1_g8 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r1_g8_id',verbose_name="Top Left Round 1 Game 8 Winner")
	bottom_left_r1_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r1_g1_id',verbose_name="Bottom Left Round 1 Game 1 Winner")
	bottom_left_r1_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r1_g2_id',verbose_name="Bottom Left Round 1 Game 2 Winner")
	bottom_left_r1_g3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r1_g3_id',verbose_name="Bottom Left Round 1 Game 3 Winner")
	bottom_left_r1_g4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r1_g4_id',verbose_name="Bottom Left Round 1 Game 4 Winner")
	bottom_left_r1_g5 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r1_g5_id',verbose_name="Bottom Left Round 1 Game 5 Winner")
	bottom_left_r1_g6 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r1_g6_id',verbose_name="Bottom Left Round 1 Game 6 Winner")
	bottom_left_r1_g7 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r1_g7_id',verbose_name="Bottom Left Round 1 Game 7 Winner")
	bottom_left_r1_g8 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r1_g8_id',verbose_name="Bottom Left Round 1 Game 8 Winner")
	top_right_r1_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r1_g1_id',verbose_name="Top Right Round 1 Game 1 Winner")
	top_right_r1_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r1_g2_id',verbose_name="Top Right Round 1 Game 2 Winner")
	top_right_r1_g3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r1_g3_id',verbose_name="Top Right Round 1 Game 3 Winner")
	top_right_r1_g4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r1_g4_id',verbose_name="Top Right Round 1 Game 4 Winner")
	top_right_r1_g5 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r1_g5_id',verbose_name="Top Right Round 1 Game 5 Winner")
	top_right_r1_g6 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r1_g6_id',verbose_name="Top Right Round 1 Game 6 Winner")
	top_right_r1_g7 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r1_g7_id',verbose_name="Top Right Round 1 Game 7 Winner")
	top_right_r1_g8 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r1_g8_id',verbose_name="Top Right Round 1 Game 8 Winner")
	bottom_right_r1_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r1_g1_id',verbose_name="Bottom Right Round 1 Game 1 Winner")
	bottom_right_r1_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r1_g2_id',verbose_name="Bottom Right Round 1 Game 2 Winner")
	bottom_right_r1_g3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r1_g3_id',verbose_name="Bottom Right Round 1 Game 3 Winner")
	bottom_right_r1_g4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r1_g4_id',verbose_name="Bottom Right Round 1 Game 4 Winner")
	bottom_right_r1_g5 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r1_g5_id',verbose_name="Bottom Right Round 1 Game 5 Winner")
	bottom_right_r1_g6 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r1_g6_id',verbose_name="Bottom Right Round 1 Game 6 Winner")
	bottom_right_r1_g7 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r1_g7_id',verbose_name="Bottom Right Round 1 Game 7 Winner")
	bottom_right_r1_g8 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r1_g8_id',verbose_name="Bottom Right Round 1 Game 8 Winner")
	top_left_r2_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r2_g1_id',verbose_name="Top Left Round 2 Game 1 Winner")
	top_left_r2_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r2_g2_id',verbose_name="Top Left Round 2 Game 2 Winner")
	top_left_r2_g3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r2_g3_id',verbose_name="Top Left Round 2 Game 3 Winner")
	top_left_r2_g4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_r2_g4_id',verbose_name="Top Left Round 2 Game 4 Winner")
	bottom_left_r2_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r2_g1_id',verbose_name="Bottom Left Round 2 Game 1 Winner")
	bottom_left_r2_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r2_g2_id',verbose_name="Bottom Left Round 2 Game 2 Winner")
	bottom_left_r2_g3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r2_g3_id',verbose_name="Bottom Left Round 2 Game 3 Winner")
	bottom_left_r2_g4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_r2_g4_id',verbose_name="Bottom Left Round 2 Game 4 Winner")
	top_right_r2_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r2_g1_id',verbose_name="Top Right Round 2 Game 1 Winner")
	top_right_r2_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r2_g2_id',verbose_name="Top Right Round 2 Game 2 Winner")
	top_right_r2_g3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r2_g3_id',verbose_name="Top Right Round 2 Game 3 Winner")
	top_right_r2_g4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_r2_g4_id',verbose_name="Top Right Round 2 Game 4 Winner")
	bottom_right_r2_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r2_g1_id',verbose_name="Bottom Right Round 2 Game 1 Winner")
	bottom_right_r2_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r2_g2_id',verbose_name="Bottom Right Round 2 Game 2 Winner")
	bottom_right_r2_g3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r2_g3_id',verbose_name="Bottom Right Round 2 Game 3 Winner")
	bottom_right_r2_g4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_r2_g4_id',verbose_name="Bottom Right Round 2 Game 4 Winner")
	top_left_ss_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_ss_g1_id',verbose_name="Top Left Sweet 16 Game 1 Winner")
	top_left_ss_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_ss_g2_id',verbose_name="Top Left Sweet 16 Game 2 Winner")
	bottom_left_ss_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_ss_g1_id',verbose_name="Bottom Left Sweet 16 Game 1 Winner")
	bottom_left_ss_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_ss_g2_id',verbose_name="Bottom Left Sweet 16 Game 2 Winner")
	top_right_ss_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_ss_g1_id',verbose_name="Top Right Sweet 16 Game 1 Winner")
	top_right_ss_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_ss_g2_id',verbose_name="Top Right Sweet 16 Game 2 Winner")
	bottom_right_ss_g1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_ss_g1_id',verbose_name="Bottom Right Sweet 16 Game 1 Winner")
	bottom_right_ss_g2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_ss_g2_id',verbose_name="Bottom Right Sweet 16 Game 2 Winner")
	top_left_ee = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_ee_id',verbose_name="Top Left Elite Eight Winner")
	bottom_left_ee = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_ee_id',verbose_name="Bottom Left Elite Eight Winner")
	top_right_ee = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_ee_id',verbose_name="Top Right Elite Eight Winner")
	bottom_right_ee = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_ee_id',verbose_name="Bottom Right Elite Eight Winner")
	ff_left = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='ff_left_id',verbose_name="Left Final Four Winner")
	ff_right = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='ff_right_id',verbose_name="Right Final Four Winner")
	championship = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='championship_id',verbose_name="National Champion")
	top_left_r1_g1_correct =  models.BooleanField(default=True)
	top_left_r1_g2_correct =  models.BooleanField(default=True)
	top_left_r1_g3_correct =  models.BooleanField(default=True)
	top_left_r1_g4_correct =  models.BooleanField(default=True)
	top_left_r1_g5_correct =  models.BooleanField(default=True)
	top_left_r1_g6_correct =  models.BooleanField(default=True)
	top_left_r1_g7_correct =  models.BooleanField(default=True)
	top_left_r1_g8_correct =  models.BooleanField(default=True)
	bottom_left_r1_g1_correct =  models.BooleanField(default=True)
	bottom_left_r1_g2_correct =  models.BooleanField(default=True)
	bottom_left_r1_g3_correct =  models.BooleanField(default=True)
	bottom_left_r1_g4_correct =  models.BooleanField(default=True)
	bottom_left_r1_g5_correct =  models.BooleanField(default=True)
	bottom_left_r1_g6_correct =  models.BooleanField(default=True)
	bottom_left_r1_g7_correct =  models.BooleanField(default=True)
	bottom_left_r1_g8_correct =  models.BooleanField(default=True)
	top_right_r1_g1_correct =  models.BooleanField(default=True)
	top_right_r1_g2_correct =  models.BooleanField(default=True)
	top_right_r1_g3_correct =  models.BooleanField(default=True)
	top_right_r1_g4_correct =  models.BooleanField(default=True)
	top_right_r1_g5_correct =  models.BooleanField(default=True)
	top_right_r1_g6_correct =  models.BooleanField(default=True)
	top_right_r1_g7_correct =  models.BooleanField(default=True)
	top_right_r1_g8_correct =  models.BooleanField(default=True)
	bottom_right_r1_g1_correct =  models.BooleanField(default=True)
	bottom_right_r1_g2_correct =  models.BooleanField(default=True)
	bottom_right_r1_g3_correct =  models.BooleanField(default=True)
	bottom_right_r1_g4_correct =  models.BooleanField(default=True)
	bottom_right_r1_g5_correct =  models.BooleanField(default=True)
	bottom_right_r1_g6_correct =  models.BooleanField(default=True)
	bottom_right_r1_g7_correct =  models.BooleanField(default=True)
	bottom_right_r1_g8_correct =  models.BooleanField(default=True)
	top_left_r2_g1_correct =  models.BooleanField(default=True)
	top_left_r2_g2_correct =  models.BooleanField(default=True)
	top_left_r2_g3_correct =  models.BooleanField(default=True)
	top_left_r2_g4_correct =  models.BooleanField(default=True)
	bottom_left_r2_g1_correct =  models.BooleanField(default=True)
	bottom_left_r2_g2_correct =  models.BooleanField(default=True)
	bottom_left_r2_g3_correct =  models.BooleanField(default=True)
	bottom_left_r2_g4_correct =  models.BooleanField(default=True)
	top_right_r2_g1_correct =  models.BooleanField(default=True)
	top_right_r2_g2_correct =  models.BooleanField(default=True)
	top_right_r2_g3_correct =  models.BooleanField(default=True)
	top_right_r2_g4_correct =  models.BooleanField(default=True)
	bottom_right_r2_g1_correct =  models.BooleanField(default=True)
	bottom_right_r2_g2_correct =  models.BooleanField(default=True)
	bottom_right_r2_g3_correct =  models.BooleanField(default=True)
	bottom_right_r2_g4_correct =  models.BooleanField(default=True)
	top_left_ss_g1_correct =  models.BooleanField(default=True)
	top_left_ss_g2_correct =  models.BooleanField(default=True)
	bottom_left_ss_g1_correct =  models.BooleanField(default=True)
	bottom_left_ss_g2_correct =  models.BooleanField(default=True)
	top_right_ss_g1_correct =  models.BooleanField(default=True)
	top_right_ss_g2_correct =  models.BooleanField(default=True)
	bottom_right_ss_g1_correct =  models.BooleanField(default=True)
	bottom_right_ss_g2_correct =  models.BooleanField(default=True)
	top_left_ee_correct =  models.BooleanField(default=True)
	bottom_left_ee_correct =  models.BooleanField(default=True)
	top_right_ee_correct =  models.BooleanField(default=True)
	bottom_right_ee_correct =  models.BooleanField(default=True)
	ff_left_correct =  models.BooleanField(default=True)
	ff_right_correct =  models.BooleanField(default=True)
	championship_correct =  models.BooleanField(default=True)

	def __str__(self):
		"""
		Display the name and year when a bracket is printed.
		"""
		return self.name + ' - ' + str(self.year)

	class Meta:
		"""
		Order brackets by year (starting from most recent) when listing.
		"""
		ordering = ["-year"]

	def calculate_score(self):
		"""
		Use the correctness fields to calculate the overall score for a bracket.
		Round 1 wins = 1 point, Round 2 wins = 2 points, Sweet 16 wins = 4 points,
		Elite Eight wins = 8 points, Final Four wins = 16 point, National championship
		win = 32 points.
		"""
		score = int(self.top_left_r1_g1_correct) + int(self.top_left_r1_g2_correct) + int(self.top_left_r1_g3_correct) + int(self.top_left_r1_g4_correct)
		score += int(self.top_left_r1_g5_correct) + int(self.top_left_r1_g6_correct) + int(self.top_left_r1_g7_correct) + int(self.top_left_r1_g8_correct)
		score += int(self.bottom_left_r1_g1_correct) + int(self.bottom_left_r1_g2_correct) + int(self.bottom_left_r1_g3_correct) + int(self.bottom_left_r1_g4_correct)
		score += int(self.bottom_left_r1_g5_correct) + int(self.bottom_left_r1_g6_correct) + int(self.bottom_left_r1_g7_correct) + int(self.bottom_left_r1_g8_correct)
		score += int(self.top_right_r1_g1_correct) + int(self.top_right_r1_g2_correct) + int(self.top_right_r1_g3_correct) + int(self.top_right_r1_g4_correct)
		score += int(self.top_right_r1_g5_correct) + int(self.top_right_r1_g6_correct) + int(self.top_right_r1_g7_correct) + int(self.top_right_r1_g8_correct)
		score += int(self.bottom_right_r1_g1_correct) + int(self.bottom_right_r1_g2_correct) + int(self.bottom_right_r1_g3_correct) + int(self.bottom_right_r1_g4_correct)
		score += int(self.bottom_right_r1_g5_correct) + int(self.bottom_right_r1_g6_correct) + int(self.bottom_right_r1_g7_correct) + int(self.bottom_right_r1_g8_correct)
		score += 2*(int(self.top_left_r2_g1_correct) + int(self.top_left_r2_g2_correct) + int(self.top_left_r2_g3_correct) + int(self.top_left_r2_g4_correct))
		score += 2*(int(self.bottom_left_r2_g1_correct) + int(self.bottom_left_r2_g2_correct) + int(self.bottom_left_r2_g3_correct) + int(self.bottom_left_r2_g4_correct))
		score += 2*(int(self.top_right_r2_g1_correct) + int(self.top_right_r2_g2_correct) + int(self.top_right_r2_g3_correct) + int(self.top_right_r2_g4_correct))
		score += 2*(int(self.bottom_right_r2_g1_correct) + int(self.bottom_right_r2_g2_correct) + int(self.bottom_right_r2_g3_correct) + int(self.bottom_right_r2_g4_correct))
		score += 4*(int(self.top_left_ss_g1_correct) + int(self.top_left_ss_g2_correct))
		score += 4*(int(self.bottom_left_ss_g1_correct) + int(self.bottom_left_ss_g2_correct))
		score += 4*(int(self.top_right_ss_g1_correct) + int(self.top_right_ss_g2_correct))
		score += 4*(int(self.bottom_right_ss_g1_correct) + int(self.bottom_right_ss_g2_correct))
		score += 8*(int(self.top_left_ee_correct) + int(self.bottom_left_ee_correct) + int(self.top_right_ee_correct) + int(self.bottom_right_ee_correct))
		score += 16*(int(self.ff_left_correct) + int(self.ff_right_correct))
		score += 32*(int(self.championship_correct))
		return score

	def calculate_correctness(self):
		"""
		Compare a bracket to the true outcome of the tournament and set each
		correctness variables based on what actually happened.
		"""

		real = Bracket.objects.get(year=self.year, name='TRUTH') #what actually happened
		self.top_left_r1_g1_correct = True if real.top_left_r1_g1 == self.top_left_r1_g1 else False
		self.top_left_r1_g2_correct = True if real.top_left_r1_g2 == self.top_left_r1_g2 else False
		self.top_left_r1_g3_correct = True if real.top_left_r1_g3 == self.top_left_r1_g3 else False
		self.top_left_r1_g4_correct = True if real.top_left_r1_g4 == self.top_left_r1_g4 else False
		self.top_left_r1_g5_correct = True if real.top_left_r1_g5 == self.top_left_r1_g5 else False
		self.top_left_r1_g6_correct = True if real.top_left_r1_g6 == self.top_left_r1_g6 else False
		self.top_left_r1_g7_correct = True if real.top_left_r1_g7 == self.top_left_r1_g7 else False
		self.top_left_r1_g8_correct = True if real.top_left_r1_g8 == self.top_left_r1_g8 else False
		self.bottom_left_r1_g1_correct = True if real.bottom_left_r1_g1 == self.bottom_left_r1_g1 else False
		self.bottom_left_r1_g2_correct = True if real.bottom_left_r1_g2 == self.bottom_left_r1_g2 else False
		self.bottom_left_r1_g3_correct = True if real.bottom_left_r1_g3 == self.bottom_left_r1_g3 else False
		self.bottom_left_r1_g4_correct = True if real.bottom_left_r1_g4 == self.bottom_left_r1_g4 else False
		self.bottom_left_r1_g5_correct = True if real.bottom_left_r1_g5 == self.bottom_left_r1_g5 else False
		self.bottom_left_r1_g6_correct = True if real.bottom_left_r1_g6 == self.bottom_left_r1_g6 else False
		self.bottom_left_r1_g7_correct = True if real.bottom_left_r1_g7 == self.bottom_left_r1_g7 else False
		self.bottom_left_r1_g8_correct = True if real.bottom_left_r1_g8 == self.bottom_left_r1_g8 else False
		self.top_right_r1_g1_correct = True if real.top_right_r1_g1 == self.top_right_r1_g1 else False
		self.top_right_r1_g2_correct = True if real.top_right_r1_g2 == self.top_right_r1_g2 else False
		self.top_right_r1_g3_correct = True if real.top_right_r1_g3 == self.top_right_r1_g3 else False
		self.top_right_r1_g4_correct = True if real.top_right_r1_g4 == self.top_right_r1_g4 else False
		self.top_right_r1_g5_correct = True if real.top_right_r1_g5 == self.top_right_r1_g5 else False
		self.top_right_r1_g6_correct = True if real.top_right_r1_g6 == self.top_right_r1_g6 else False
		self.top_right_r1_g7_correct = True if real.top_right_r1_g7 == self.top_right_r1_g7 else False
		self.top_right_r1_g8_correct = True if real.top_right_r1_g8 == self.top_right_r1_g8 else False
		self.bottom_right_r1_g1_correct = True if real.bottom_right_r1_g1 == self.bottom_right_r1_g1 else False
		self.bottom_right_r1_g2_correct = True if real.bottom_right_r1_g2 == self.bottom_right_r1_g2 else False
		self.bottom_right_r1_g3_correct = True if real.bottom_right_r1_g3 == self.bottom_right_r1_g3 else False
		self.bottom_right_r1_g4_correct = True if real.bottom_right_r1_g4 == self.bottom_right_r1_g4 else False
		self.bottom_right_r1_g5_correct = True if real.bottom_right_r1_g5 == self.bottom_right_r1_g5 else False
		self.bottom_right_r1_g6_correct = True if real.bottom_right_r1_g6 == self.bottom_right_r1_g6 else False
		self.bottom_right_r1_g7_correct = True if real.bottom_right_r1_g7 == self.bottom_right_r1_g7 else False
		self.bottom_right_r1_g8_correct = True if real.bottom_right_r1_g8 == self.bottom_right_r1_g8 else False
		self.top_left_r2_g1_correct = True if real.top_left_r2_g1 == self.top_left_r2_g1 else False
		self.top_left_r2_g2_correct = True if real.top_left_r2_g2 == self.top_left_r2_g2 else False
		self.top_left_r2_g3_correct = True if real.top_left_r2_g3 == self.top_left_r2_g3 else False
		self.top_left_r2_g4_correct = True if real.top_left_r2_g4 == self.top_left_r2_g4 else False
		self.bottom_left_r2_g1_correct = True if real.bottom_left_r2_g1 == self.bottom_left_r2_g1 else False
		self.bottom_left_r2_g2_correct = True if real.bottom_left_r2_g2 == self.bottom_left_r2_g2 else False
		self.bottom_left_r2_g3_correct = True if real.bottom_left_r2_g3 == self.bottom_left_r2_g3 else False
		self.bottom_left_r2_g4_correct = True if real.bottom_left_r2_g4 == self.bottom_left_r2_g4 else False
		self.top_right_r2_g1_correct = True if real.top_right_r2_g1 == self.top_right_r2_g1 else False
		self.top_right_r2_g2_correct = True if real.top_right_r2_g2 == self.top_right_r2_g2 else False
		self.top_right_r2_g3_correct = True if real.top_right_r2_g3 == self.top_right_r2_g3 else False
		self.top_right_r2_g4_correct = True if real.top_right_r2_g4 == self.top_right_r2_g4 else False
		self.bottom_right_r2_g1_correct = True if real.bottom_right_r2_g1 == self.bottom_right_r2_g1 else False
		self.bottom_right_r2_g2_correct = True if real.bottom_right_r2_g2 == self.bottom_right_r2_g2 else False
		self.bottom_right_r2_g3_correct = True if real.bottom_right_r2_g3 == self.bottom_right_r2_g3 else False
		self.bottom_right_r2_g4_correct = True if real.bottom_right_r2_g4 == self.bottom_right_r2_g4 else False
		self.top_left_ss_g1_correct = True if real.top_left_ss_g1 == self.top_left_ss_g1 else False
		self.top_left_ss_g2_correct = True if real.top_left_ss_g2 == self.top_left_ss_g2 else False
		self.bottom_left_ss_g1_correct = True if real.bottom_left_ss_g1 == self.bottom_left_ss_g1 else False
		self.bottom_left_ss_g2_correct = True if real.bottom_left_ss_g2 == self.bottom_left_ss_g2 else False
		self.top_right_ss_g1_correct = True if real.top_right_ss_g1 == self.top_right_ss_g1 else False
		self.top_right_ss_g2_correct = True if real.top_right_ss_g2 == self.top_right_ss_g2 else False
		self.bottom_right_ss_g1_correct = True if real.bottom_right_ss_g1 == self.bottom_right_ss_g1 else False
		self.bottom_right_ss_g2_correct = True if real.bottom_right_ss_g2 == self.bottom_right_ss_g2 else False
		self.top_left_ee_correct = True if real.top_left_ee == self.top_left_ee else False
		self.bottom_left_ee_correct = True if real.bottom_left_ee == self.bottom_left_ee else False
		self.top_right_ee_correct = True if real.top_right_ee == self.top_right_ee else False
		self.bottom_right_ee_correct = True if real.bottom_right_ee == self.bottom_right_ee else False
		self.ff_left_correct = True if real.ff_left == self.ff_left else False
		self.ff_right_correct = True if real.ff_right == self.ff_right else False
		self.championship_correct = True if real.championship == self.championship else False

	def num_upsets(self):
		"""
		Determine how many of the games were (or were predicted to be) upsets
		"""
		stats = Season_stats.objects.filter(year=self.year).exclude(made_tournament = False).all()
		starting64 = Tournament.objects.get(year=self.year)
		seed = {}
		for stat in stats:
			seed[stat.team] = stat.tournament_seed
		upsets = 0
		upsets = upsets + int(seed[self.top_left_r1_g1] == 16)
		upsets = upsets + int(seed[self.top_left_r1_g2] == 9)
		upsets = upsets + int(seed[self.top_left_r1_g3] == 12)
		upsets = upsets + int(seed[self.top_left_r1_g4] == 13)
		upsets = upsets + int(seed[self.top_left_r1_g5] == 11)
		upsets = upsets + int(seed[self.top_left_r1_g6] == 14)
		upsets = upsets + int(seed[self.top_left_r1_g7] == 10)
		upsets = upsets + int(seed[self.top_left_r1_g8] == 15)
		upsets = upsets + int(seed[self.bottom_left_r1_g1] == 16)
		upsets = upsets + int(seed[self.bottom_left_r1_g2] == 9)
		upsets = upsets + int(seed[self.bottom_left_r1_g3] == 12)
		upsets = upsets + int(seed[self.bottom_left_r1_g4] == 13)
		upsets = upsets + int(seed[self.bottom_left_r1_g5] == 11)
		upsets = upsets + int(seed[self.bottom_left_r1_g6] == 14)
		upsets = upsets + int(seed[self.bottom_left_r1_g7] == 10)
		upsets = upsets + int(seed[self.bottom_left_r1_g8] == 15)
		upsets = upsets + int(seed[self.top_right_r1_g1] == 16)
		upsets = upsets + int(seed[self.top_right_r1_g2] == 9)
		upsets = upsets + int(seed[self.top_right_r1_g3] == 12)
		upsets = upsets + int(seed[self.top_right_r1_g4] == 13)
		upsets = upsets + int(seed[self.top_right_r1_g5] == 11)
		upsets = upsets + int(seed[self.top_right_r1_g6] == 14)
		upsets = upsets + int(seed[self.top_right_r1_g7] == 10)
		upsets = upsets + int(seed[self.top_right_r1_g8] == 15)
		upsets = upsets + int(seed[self.bottom_right_r1_g1] == 16)
		upsets = upsets + int(seed[self.bottom_right_r1_g2] == 9)
		upsets = upsets + int(seed[self.bottom_right_r1_g3] == 12)
		upsets = upsets + int(seed[self.bottom_right_r1_g4] == 13)
		upsets = upsets + int(seed[self.bottom_right_r1_g5] == 11)
		upsets = upsets + int(seed[self.bottom_right_r1_g6] == 14)
		upsets = upsets + int(seed[self.bottom_right_r1_g7] == 10)
		upsets = upsets + int(seed[self.bottom_right_r1_g8] == 15)
		upsets = upsets + int((seed[self.top_left_r2_g1] > seed[self.top_left_r1_g1]) or (seed[self.top_left_r2_g1] > seed[self.top_left_r1_g2]))
		upsets = upsets + int((seed[self.top_left_r2_g2] > seed[self.top_left_r1_g3]) or (seed[self.top_left_r2_g2] > seed[self.top_left_r1_g4]))
		upsets = upsets + int((seed[self.top_left_r2_g3] > seed[self.top_left_r1_g5]) or (seed[self.top_left_r2_g3] > seed[self.top_left_r1_g6]))
		upsets = upsets + int((seed[self.top_left_r2_g4] > seed[self.top_left_r1_g7]) or (seed[self.top_left_r2_g4] > seed[self.top_left_r1_g8]))
		upsets = upsets + int((seed[self.bottom_left_r2_g1] > seed[self.bottom_left_r1_g1]) or (seed[self.bottom_left_r2_g1] > seed[self.bottom_left_r1_g2]))
		upsets = upsets + int((seed[self.bottom_left_r2_g2] > seed[self.bottom_left_r1_g3]) or (seed[self.bottom_left_r2_g2] > seed[self.bottom_left_r1_g4]))
		upsets = upsets + int((seed[self.bottom_left_r2_g3] > seed[self.bottom_left_r1_g5]) or (seed[self.bottom_left_r2_g3] > seed[self.bottom_left_r1_g6]))
		upsets = upsets + int((seed[self.bottom_left_r2_g4] > seed[self.bottom_left_r1_g7]) or (seed[self.bottom_left_r2_g4] > seed[self.bottom_left_r1_g8]))
		upsets = upsets + int((seed[self.top_right_r2_g1] > seed[self.top_right_r1_g1]) or (seed[self.top_right_r2_g1] > seed[self.top_right_r1_g2]))
		upsets = upsets + int((seed[self.top_right_r2_g2] > seed[self.top_right_r1_g3]) or (seed[self.top_right_r2_g2] > seed[self.top_right_r1_g4]))
		upsets = upsets + int((seed[self.top_right_r2_g3] > seed[self.top_right_r1_g5]) or (seed[self.top_right_r2_g3] > seed[self.top_right_r1_g6]))
		upsets = upsets + int((seed[self.top_right_r2_g4] > seed[self.top_right_r1_g7]) or (seed[self.top_right_r2_g4] > seed[self.top_right_r1_g8]))
		upsets = upsets + int((seed[self.bottom_right_r2_g1] > seed[self.bottom_right_r1_g1]) or (seed[self.bottom_right_r2_g1] > seed[self.bottom_right_r1_g2]))
		upsets = upsets + int((seed[self.bottom_right_r2_g2] > seed[self.bottom_right_r1_g3]) or (seed[self.bottom_right_r2_g2] > seed[self.bottom_right_r1_g4]))
		upsets = upsets + int((seed[self.bottom_right_r2_g3] > seed[self.bottom_right_r1_g5]) or (seed[self.bottom_right_r2_g3] > seed[self.bottom_right_r1_g6]))
		upsets = upsets + int((seed[self.bottom_right_r2_g4] > seed[self.bottom_right_r1_g7]) or (seed[self.bottom_right_r2_g4] > seed[self.bottom_right_r1_g8]))
		upsets = upsets + int((seed[self.top_left_ss_g1] > seed[self.top_left_r2_g1]) or (seed[self.top_left_ss_g1] > seed[self.top_left_r2_g2]))
		upsets = upsets + int((seed[self.top_left_ss_g2] > seed[self.top_left_r2_g3]) or (seed[self.top_left_ss_g2] > seed[self.top_left_r2_g4]))
		upsets = upsets + int((seed[self.bottom_left_ss_g1] > seed[self.bottom_left_r2_g1]) or (seed[self.bottom_left_ss_g1] > seed[self.bottom_left_r2_g2]))
		upsets = upsets + int((seed[self.bottom_left_ss_g2] > seed[self.bottom_left_r2_g3]) or (seed[self.bottom_left_ss_g2] > seed[self.bottom_left_r2_g4]))
		upsets = upsets + int((seed[self.top_right_ss_g1] > seed[self.top_right_r2_g1]) or (seed[self.top_right_ss_g1] > seed[self.top_right_r2_g2]))
		upsets = upsets + int((seed[self.top_right_ss_g2] > seed[self.top_right_r2_g3]) or (seed[self.top_right_ss_g2] > seed[self.top_right_r2_g4]))
		upsets = upsets + int((seed[self.bottom_right_ss_g1] > seed[self.bottom_right_r2_g1]) or (seed[self.bottom_right_ss_g1] > seed[self.bottom_right_r2_g2]))
		upsets = upsets + int((seed[self.bottom_right_ss_g2] > seed[self.bottom_right_r2_g3]) or (seed[self.bottom_right_ss_g2] > seed[self.bottom_right_r2_g4]))
		upsets = upsets + int((seed[self.top_left_ee] > seed[self.top_left_ss_g1]) or (seed[self.top_left_ee] > seed[self.top_left_ss_g2]))
		upsets = upsets + int((seed[self.bottom_left_ee] > seed[self.bottom_left_ss_g1]) or (seed[self.bottom_left_ee] > seed[self.bottom_left_ss_g2]))
		upsets = upsets + int((seed[self.top_right_ee] > seed[self.top_right_ss_g1]) or (seed[self.top_right_ee] > seed[self.top_right_ss_g2]))
		upsets = upsets + int((seed[self.bottom_right_ee] > seed[self.bottom_right_ss_g1]) or (seed[self.bottom_right_ee] > seed[self.bottom_right_ss_g2]))
		upsets = upsets + int((seed[self.ff_left] > seed[self.top_left_ee]) or (seed[self.ff_left] > seed[self.bottom_left_ee]))
		upsets = upsets + int((seed[self.ff_right] > seed[self.top_right_ee]) or (seed[self.ff_right] > seed[self.bottom_right_ee]))
		upsets = upsets + int((seed[self.championship] > seed[self.ff_left]) or (seed[self.championship] > seed[self.ff_right]))
		return upsets

	def num_correct_upsets(self):
		"""
		Determine how many of the actual upsets were predicted
		"""
		if self.name == "TRUTH":
			return -1
		true = Bracket.objects.filter(name="TRUTH").get(year=self.year)
		stats = Season_stats.objects.filter(year=self.year).exclude(made_tournament = False).all()
		starting64 = Tournament.objects.get(year=self.year)
		seed = {}
		for stat in stats:
			seed[stat.team] = stat.tournament_seed
		upsets = 0
		upsets = upsets + int(seed[self.top_left_r1_g1] == 16 and self.top_left_r1_g1_correct)
		upsets = upsets + int(seed[self.top_left_r1_g2] == 9 and self.top_left_r1_g2_correct)
		upsets = upsets + int(seed[self.top_left_r1_g3] == 12 and self.top_left_r1_g3_correct)
		upsets = upsets + int(seed[self.top_left_r1_g4] == 13 and self.top_left_r1_g4_correct)
		upsets = upsets + int(seed[self.top_left_r1_g5] == 11 and self.top_left_r1_g5_correct)
		upsets = upsets + int(seed[self.top_left_r1_g6] == 14 and self.top_left_r1_g6_correct)
		upsets = upsets + int(seed[self.top_left_r1_g7] == 10 and self.top_left_r1_g7_correct)
		upsets = upsets + int(seed[self.top_left_r1_g8] == 15 and self.top_left_r1_g8_correct)
		upsets = upsets + int(seed[self.bottom_left_r1_g1] == 16 and self.bottom_left_r1_g1_correct)
		upsets = upsets + int(seed[self.bottom_left_r1_g2] == 9 and self.bottom_left_r1_g2_correct)
		upsets = upsets + int(seed[self.bottom_left_r1_g3] == 12 and self.bottom_left_r1_g3_correct)
		upsets = upsets + int(seed[self.bottom_left_r1_g4] == 13 and self.bottom_left_r1_g4_correct)
		upsets = upsets + int(seed[self.bottom_left_r1_g5] == 11 and self.bottom_left_r1_g5_correct)
		upsets = upsets + int(seed[self.bottom_left_r1_g6] == 14 and self.bottom_left_r1_g6_correct)
		upsets = upsets + int(seed[self.bottom_left_r1_g7] == 10 and self.bottom_left_r1_g7_correct)
		upsets = upsets + int(seed[self.bottom_left_r1_g8] == 15 and self.bottom_left_r1_g8_correct)
		upsets = upsets + int(seed[self.top_right_r1_g1] == 16 and self.top_right_r1_g1_correct)
		upsets = upsets + int(seed[self.top_right_r1_g2] == 9 and self.top_right_r1_g2_correct)
		upsets = upsets + int(seed[self.top_right_r1_g3] == 12 and self.top_right_r1_g3_correct)
		upsets = upsets + int(seed[self.top_right_r1_g4] == 13 and self.top_right_r1_g4_correct)
		upsets = upsets + int(seed[self.top_right_r1_g5] == 11 and self.top_right_r1_g5_correct)
		upsets = upsets + int(seed[self.top_right_r1_g6] == 14 and self.top_right_r1_g6_correct)
		upsets = upsets + int(seed[self.top_right_r1_g7] == 10 and self.top_right_r1_g7_correct)
		upsets = upsets + int(seed[self.top_right_r1_g8] == 15 and self.top_right_r1_g8_correct)
		upsets = upsets + int(seed[self.bottom_right_r1_g1] == 16 and self.bottom_right_r1_g1_correct)
		upsets = upsets + int(seed[self.bottom_right_r1_g2] == 9 and self.bottom_right_r1_g2_correct)
		upsets = upsets + int(seed[self.bottom_right_r1_g3] == 12 and self.bottom_right_r1_g3_correct)
		upsets = upsets + int(seed[self.bottom_right_r1_g4] == 13 and self.bottom_right_r1_g4_correct)
		upsets = upsets + int(seed[self.bottom_right_r1_g5] == 11 and self.bottom_right_r1_g5_correct)
		upsets = upsets + int(seed[self.bottom_right_r1_g6] == 14 and self.bottom_right_r1_g6_correct)
		upsets = upsets + int(seed[self.bottom_right_r1_g7] == 10 and self.bottom_right_r1_g7_correct)
		upsets = upsets + int(seed[self.bottom_right_r1_g8] == 15 and self.bottom_right_r1_g8_correct)
		upsets = upsets + int((true.top_left_r2_g1 == self.top_left_r2_g1) and ((seed[true.top_left_r2_g1] > seed[true.top_left_r1_g1]) or (seed[true.top_left_r2_g1] > seed[true.top_left_r1_g2])))
		upsets = upsets + int((true.top_left_r2_g2 == self.top_left_r2_g2) and ((seed[true.top_left_r2_g2] > seed[true.top_left_r1_g3]) or (seed[true.top_left_r2_g2] > seed[true.top_left_r1_g4])))
		upsets = upsets + int((true.top_left_r2_g3 == self.top_left_r2_g3) and ((seed[true.top_left_r2_g3] > seed[true.top_left_r1_g5]) or (seed[true.top_left_r2_g3] > seed[true.top_left_r1_g6])))
		upsets = upsets + int((true.top_left_r2_g4 == self.top_left_r2_g4) and ((seed[true.top_left_r2_g4] > seed[true.top_left_r1_g7]) or (seed[true.top_left_r2_g4] > seed[true.top_left_r1_g8])))
		upsets = upsets + int((true.bottom_left_r2_g1 == self.bottom_left_r2_g1) and ((seed[true.bottom_left_r2_g1] > seed[true.bottom_left_r1_g1]) or (seed[true.bottom_left_r2_g1] > seed[true.bottom_left_r1_g2])))
		upsets = upsets + int((true.bottom_left_r2_g2 == self.bottom_left_r2_g2) and ((seed[true.bottom_left_r2_g2] > seed[true.bottom_left_r1_g3]) or (seed[true.bottom_left_r2_g2] > seed[true.bottom_left_r1_g4])))
		upsets = upsets + int((true.bottom_left_r2_g3 == self.bottom_left_r2_g3) and ((seed[true.bottom_left_r2_g3] > seed[true.bottom_left_r1_g5]) or (seed[true.bottom_left_r2_g3] > seed[true.bottom_left_r1_g6])))
		upsets = upsets + int((true.bottom_left_r2_g4 == self.bottom_left_r2_g4) and ((seed[true.bottom_left_r2_g4] > seed[true.bottom_left_r1_g7]) or (seed[true.bottom_left_r2_g4] > seed[true.bottom_left_r1_g8])))
		upsets = upsets + int((true.top_right_r2_g1 == self.top_right_r2_g1) and ((seed[true.top_right_r2_g1] > seed[true.top_right_r1_g1]) or (seed[true.top_right_r2_g1] > seed[true.top_right_r1_g2])))
		upsets = upsets + int((true.top_right_r2_g2 == self.top_right_r2_g2) and ((seed[true.top_right_r2_g2] > seed[true.top_right_r1_g3]) or (seed[true.top_right_r2_g2] > seed[true.top_right_r1_g4])))
		upsets = upsets + int((true.top_right_r2_g3 == self.top_right_r2_g3) and ((seed[true.top_right_r2_g3] > seed[true.top_right_r1_g5]) or (seed[true.top_right_r2_g3] > seed[true.top_right_r1_g6])))
		upsets = upsets + int((true.top_right_r2_g4 == self.top_right_r2_g4) and ((seed[true.top_right_r2_g4] > seed[true.top_right_r1_g7]) or (seed[true.top_right_r2_g4] > seed[true.top_right_r1_g8])))
		upsets = upsets + int((true.bottom_right_r2_g1 == self.bottom_right_r2_g1) and ((seed[true.bottom_right_r2_g1] > seed[true.bottom_right_r1_g1]) or (seed[true.bottom_right_r2_g1] > seed[true.bottom_right_r1_g2])))
		upsets = upsets + int((true.bottom_right_r2_g2 == self.bottom_right_r2_g2) and ((seed[true.bottom_right_r2_g2] > seed[true.bottom_right_r1_g3]) or (seed[true.bottom_right_r2_g2] > seed[true.bottom_right_r1_g4])))
		upsets = upsets + int((true.bottom_right_r2_g3 == self.bottom_right_r2_g3) and ((seed[true.bottom_right_r2_g3] > seed[true.bottom_right_r1_g5]) or (seed[true.bottom_right_r2_g3] > seed[true.bottom_right_r1_g6])))
		upsets = upsets + int((true.bottom_right_r2_g4 == self.bottom_right_r2_g4) and ((seed[true.bottom_right_r2_g4] > seed[true.bottom_right_r1_g7]) or (seed[true.bottom_right_r2_g4] > seed[true.bottom_right_r1_g8])))
		upsets = upsets + int((true.top_left_ss_g1 == self.top_left_ss_g1) and ((seed[true.top_left_ss_g1] > seed[true.top_left_r2_g1]) or (seed[true.top_left_ss_g1] > seed[true.top_left_r2_g2])))
		upsets = upsets + int((true.top_left_ss_g2 == self.top_left_ss_g2) and ((seed[true.top_left_ss_g2] > seed[true.top_left_r2_g3]) or (seed[true.top_left_ss_g2] > seed[true.top_left_r2_g4])))
		upsets = upsets + int((true.bottom_left_ss_g1 == self.bottom_left_ss_g1) and ((seed[true.bottom_left_ss_g1] > seed[true.bottom_left_r2_g1]) or (seed[true.bottom_left_ss_g1] > seed[true.bottom_left_r2_g2])))
		upsets = upsets + int((true.bottom_left_ss_g2 == self.bottom_left_ss_g2) and ((seed[true.bottom_left_ss_g2] > seed[true.bottom_left_r2_g3]) or (seed[true.bottom_left_ss_g2] > seed[true.bottom_left_r2_g4])))
		upsets = upsets + int((true.top_right_ss_g1 == self.top_right_ss_g1) and ((seed[true.top_right_ss_g1] > seed[true.top_right_r2_g1]) or (seed[true.top_right_ss_g1] > seed[true.top_right_r2_g2])))
		upsets = upsets + int((true.top_right_ss_g2 == self.top_right_ss_g2) and ((seed[true.top_right_ss_g2] > seed[true.top_right_r2_g3]) or (seed[true.top_right_ss_g2] > seed[true.top_right_r2_g4])))
		upsets = upsets + int((true.bottom_right_ss_g1 == self.bottom_right_ss_g1) and ((seed[true.bottom_right_ss_g1] > seed[true.bottom_right_r2_g1]) or (seed[true.bottom_right_ss_g1] > seed[true.bottom_right_r2_g2])))
		upsets = upsets + int((true.bottom_right_ss_g2 == self.bottom_right_ss_g2) and ((seed[true.bottom_right_ss_g2] > seed[true.bottom_right_r2_g3]) or (seed[true.bottom_right_ss_g2] > seed[true.bottom_right_r2_g4])))
		upsets = upsets + int((true.top_left_ee == self.top_left_ee) and ((seed[true.top_left_ee] > seed[true.top_left_ss_g1]) or (seed[true.top_left_ee] > seed[true.top_left_ss_g2])))
		upsets = upsets + int((true.bottom_left_ee == self.bottom_left_ee) and ((seed[true.bottom_left_ee] > seed[true.bottom_left_ss_g1]) or (seed[true.bottom_left_ee] > seed[true.bottom_left_ss_g2])))
		upsets = upsets + int((true.top_right_ee == self.top_right_ee) and ((seed[true.top_right_ee] > seed[true.top_right_ss_g1]) or (seed[true.top_right_ee] > seed[true.top_right_ss_g2])))
		upsets = upsets + int((true.bottom_left_ee == self.bottom_left_ee) and ((seed[true.bottom_right_ee] > seed[true.bottom_right_ss_g1]) or (seed[true.bottom_right_ee] > seed[true.bottom_right_ss_g2])))
		upsets = upsets + int((true.ff_left == self.ff_left) and ((seed[true.ff_left] > seed[true.top_left_ee]) or (seed[true.ff_left] > seed[true.bottom_left_ee])))
		upsets = upsets + int((true.ff_right == self.ff_right) and ((seed[true.ff_right] > seed[true.top_right_ee]) or (seed[true.ff_right] > seed[true.bottom_right_ee])))
		upsets = upsets + int((true.championship == self.championship) and ((seed[true.championship] > seed[true.ff_left]) or (seed[true.championship] > seed[true.ff_right])))
		return upsets

	def save(self, *args, **kwargs):
		"""
		Calculate score and correctness before saving a new bracket to the
		database.
		"""

		if self.name == 'TRUTH':
			self.score = 192 #1*32 + 2*16 + 4*8 + 8*4 + 16*2 + 32*1
		else:
			self.calculate_correctness()
			self.score = self.calculate_score()
		super().save(*args, **kwargs)

class Tournament(models.Model):
	"""
	Class to represent the starting configuration of an NCAA Mens Division I
	March Madness Basketball Tournament.
	"""

	#List of region names
	EAST = 'EAST'
	MIDWEST = 'MIDWEST'
	SOUTH = 'SOUTH'
	SOUTHEAST = 'SOUTHEAST'
	SOUTHWEST = 'SOUTHWEST'
	WEST = 'WEST'

	REGION_NAMES = (
        (EAST, 'East'),
		(MIDWEST, 'Midwest'),
		(SOUTH, 'South'),
		(SOUTHEAST, 'Southeast'),
		(SOUTHWEST, 'Southwest'),
		(WEST, 'West'),
    )

	#database fields
	year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1939)],default=datetime.date.today().year, primary_key=True, unique=True)
	top_left_region = models.CharField(max_length=10,choices=REGION_NAMES,verbose_name="Top Left Region Name")
	bottom_left_region = models.CharField(max_length=10,choices=REGION_NAMES,verbose_name="Bottom Left Region Name")
	top_right_region = models.CharField(max_length=10,choices=REGION_NAMES,verbose_name="Top Right Region Name")
	bottom_right_region = models.CharField(max_length=10,choices=REGION_NAMES,verbose_name="Bottom Right Region Name")
	top_left_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_1_id',verbose_name="Top Left 1 Seed")
	top_left_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_2_id',verbose_name="Top Left 2 Seed")
	top_left_3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_3_id',verbose_name="Top Left 3 Seed")
	top_left_4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_4_id',verbose_name="Top Left 4 Seed")
	top_left_5 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_5_id',verbose_name="Top Left 5 Seed")
	top_left_6 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_6_id',verbose_name="Top Left 6 Seed")
	top_left_7 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_7_id',verbose_name="Top Left 7 Seed")
	top_left_8 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_8_id',verbose_name="Top Left 8 Seed")
	top_left_9 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_9_id',verbose_name="Top Left 9 Seed")
	top_left_10 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_10_id',verbose_name="Top Left 10 Seed")
	top_left_11 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_11_id',verbose_name="Top Left 11 Seed")
	top_left_12 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_12_id',verbose_name="Top Left 12 Seed")
	top_left_13 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_13_id',verbose_name="Top Left 13 Seed")
	top_left_14 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_14_id',verbose_name="Top Left 14 Seed")
	top_left_15 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_15_id',verbose_name="Top Left 15 Seed")
	top_left_16 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_left_16_id',verbose_name="Top Left 16 Seed")
	bottom_left_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_1_id',verbose_name="Bottom Left 1 Seed")
	bottom_left_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_2_id',verbose_name="Bottom Left 2 Seed")
	bottom_left_3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_3_id',verbose_name="Bottom Left 3 Seed")
	bottom_left_4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_4_id',verbose_name="Bottom Left 4 Seed")
	bottom_left_5 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_5_id',verbose_name="Bottom Left 5 Seed")
	bottom_left_6 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_6_id',verbose_name="Bottom Left 6 Seed")
	bottom_left_7 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_7_id',verbose_name="Bottom Left 7 Seed")
	bottom_left_8 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_8_id',verbose_name="Bottom Left 8 Seed")
	bottom_left_9 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_9_id',verbose_name="Bottom Left 9 Seed")
	bottom_left_10 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_10_id',verbose_name="Bottom Left 10 Seed")
	bottom_left_11 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_11_id',verbose_name="Bottom Left 11 Seed")
	bottom_left_12 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_12_id',verbose_name="Bottom Left 12 Seed")
	bottom_left_13 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_13_id',verbose_name="Bottom Left 13 Seed")
	bottom_left_14 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_14_id',verbose_name="Bottom Left 14 Seed")
	bottom_left_15 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_15_id',verbose_name="Bottom Left 15 Seed")
	bottom_left_16 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_left_16_id',verbose_name="Bottom Left 16 Seed")
	top_right_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_1_id',verbose_name="Top Right 1 Seed")
	top_right_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_2_id',verbose_name="Top Right 2 Seed")
	top_right_3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_3_id',verbose_name="Top Right 3 Seed")
	top_right_4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_4_id',verbose_name="Top Right 4 Seed")
	top_right_5 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_5_id',verbose_name="Top Right 5 Seed")
	top_right_6 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_6_id',verbose_name="Top Right 6 Seed")
	top_right_7 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_7_id',verbose_name="Top Right 7 Seed")
	top_right_8 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_8_id',verbose_name="Top Right 8 Seed")
	top_right_9 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_9_id',verbose_name="Top Right 9 Seed")
	top_right_10 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_10_id',verbose_name="Top Right 10 Seed")
	top_right_11 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_11_id',verbose_name="Top Right 11 Seed")
	top_right_12 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_12_id',verbose_name="Top Right 12 Seed")
	top_right_13 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_13_id',verbose_name="Top Right 13 Seed")
	top_right_14 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_14_id',verbose_name="Top Right 14 Seed")
	top_right_15 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_15_id',verbose_name="Top Right 15 Seed")
	top_right_16 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='top_right_16_id',verbose_name="Top Right 16 Seed")
	bottom_right_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_1_id',verbose_name="Bottom Right 1 Seed")
	bottom_right_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_2_id',verbose_name="Bottom Right 2 Seed")
	bottom_right_3 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_3_id',verbose_name="Bottom Right 3 Seed")
	bottom_right_4 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_4_id',verbose_name="Bottom Right 4 Seed")
	bottom_right_5 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_5_id',verbose_name="Bottom Right 5 Seed")
	bottom_right_6 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_6_id',verbose_name="Bottom Right 6 Seed")
	bottom_right_7 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_7_id',verbose_name="Bottom Right 7 Seed")
	bottom_right_8 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_8_id',verbose_name="Bottom Right 8 Seed")
	bottom_right_9 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_9_id',verbose_name="Bottom Right 9 Seed")
	bottom_right_10 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_10_id',verbose_name="Bottom Right 10 Seed")
	bottom_right_11 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_11_id',verbose_name="Bottom Right 11 Seed")
	bottom_right_12 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_12_id',verbose_name="Bottom Right 12 Seed")
	bottom_right_13 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_13_id',verbose_name="Bottom Right 13 Seed")
	bottom_right_14 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_14_id',verbose_name="Bottom Right 14 Seed")
	bottom_right_15 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_15_id',verbose_name="Bottom Right 15 Seed")
	bottom_right_16 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bottom_right_16_id',verbose_name="Bottom Right 16 Seed")

	def __str__(self):
		"""
		Display the year and the word tournament when a Tournament object is printed.
		"""
		return str(self.year) + ' Tournament'

	def getConferences(self):
		"""
		Returns a dictionary with the number of times each conference was represented
		in the tournament (for conferences that appeared at least once).
		"""
		conf_dict = {}
		for region in ["top_left","bottom_left","top_right","bottom_right"]:
			for i in range(1,17):
				conf_dict[getattr(self,"{}_{}".format(region,i)).conference] = conf_dict.get(
					getattr(self,"{}_{}".format(region,i)).conference,0) + 1
		return conf_dict

	class Meta:
		"""
		Order by year (starting with the most recent) when listing Tournament.
		"""
		ordering = ["-year"]

class Season_stats(models.Model):
	"""
	Class to keep track of a team's statistics (including tournament performance
	if applicable) for a given year.
	"""

	#database fields
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1939)],default=datetime.date.today().year)
	elo = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
	wins = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
	losses = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
	ppg = models.DecimalField(max_digits=4,decimal_places=1,validators=[MinValueValidator(0)],default=0,verbose_name="Points Per Game")
	ppga = models.DecimalField(max_digits=4,decimal_places=1,validators=[MinValueValidator(0)],default=0,verbose_name="Points Per Game Against")
	made_tournament = models.BooleanField()
	tournament_seed = models.PositiveSmallIntegerField(null=True,validators=[MinValueValidator(1),MaxValueValidator(16)])
	tournament_region = models.CharField(max_length=10,choices=Tournament.REGION_NAMES,null=True)
	tournament_wins = models.PositiveSmallIntegerField(null=True,validators=[MinValueValidator(0),MaxValueValidator(6)])
	tournament_losses = models.PositiveSmallIntegerField(null=True,validators=[MinValueValidator(0),MaxValueValidator(1)])
	tournament_lost_to = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='lost_to', null=True)

	def __str__(self):
		"""
		Display the school and season when printed
		(ex: University of Illinois 2005-2006).
		"""
		return "{} {}-{}".format(self.team,self.year - 1, self.year)

class Participant(models.Model):
	"""
	Class to keep track of overall data for my mom, aunt, and me
	"""

	PARTICIPANT_NAMES = (
        ("MOM", 'Mom'),
		("AUNT", 'Aunt'),
		("ME", 'Me'))

	#database fields
	name = models.CharField(max_length=10,choices=PARTICIPANT_NAMES)
	first_place = models.IntegerField(validators=[MinValueValidator(0)])
	second_place = models.IntegerField(validators=[MinValueValidator(0)])
	third_place = models.IntegerField(validators=[MinValueValidator(0)])
	correct_champions = models.IntegerField(validators=[MinValueValidator(0)])
	average_predicted_upsets = models.DecimalField(max_digits=3,decimal_places=1,validators=[MinValueValidator(0)])
	average_correct_upsets = models.DecimalField(max_digits=3,decimal_places=1,validators=[MinValueValidator(0)])
