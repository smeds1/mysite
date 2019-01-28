from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Bracket, Tournament

class MyBracketAdminForm(ModelForm):
	"""
	Class to properly display and validate a Bracket for insertion/deletion/
	updating on the admin page.
	"""

	class Meta:
		"""
		Declare the ordering of the Bracket fields.
		"""
		model = Bracket
		fields = ['name', 'year',
			'top_left_r1_g1','top_left_r1_g2','top_left_r1_g3','top_left_r1_g4',
			'top_left_r1_g5','top_left_r1_g6','top_left_r1_g7','top_left_r1_g8',
			'bottom_left_r1_g1','bottom_left_r1_g2','bottom_left_r1_g3','bottom_left_r1_g4',
			'bottom_left_r1_g5','bottom_left_r1_g6','bottom_left_r1_g7','bottom_left_r1_g8',
			'top_right_r1_g1','top_right_r1_g2','top_right_r1_g3','top_right_r1_g4',
			'top_right_r1_g5','top_right_r1_g6','top_right_r1_g7','top_right_r1_g8',
			'bottom_right_r1_g1','bottom_right_r1_g2','bottom_right_r1_g3','bottom_right_r1_g4',
			'bottom_right_r1_g5','bottom_right_r1_g6','bottom_right_r1_g7','bottom_right_r1_g8',
			'top_left_r2_g1','top_left_r2_g2','top_left_r2_g3','top_left_r2_g4',
			'bottom_left_r2_g1','bottom_left_r2_g2','bottom_left_r2_g3','bottom_left_r2_g4',
			'top_right_r2_g1','top_right_r2_g2','top_right_r2_g3','top_right_r2_g4',
			'bottom_right_r2_g1','bottom_right_r2_g2','bottom_right_r2_g3','bottom_right_r2_g4',
			'top_left_ss_g1','top_left_ss_g2','bottom_left_ss_g1','bottom_left_ss_g2',
			'top_right_ss_g1','top_right_ss_g2','bottom_right_ss_g1','bottom_right_ss_g2',
			'top_left_ee','bottom_left_ee','top_right_ee','bottom_right_ee',
			'ff_left','ff_right','championship']

	def clean(self):
		"""
		Verify that a bracket contains teams that are in the tournament and that
		the winner of each game was actually one of the teams playing.
		"""
		real = Tournament.objects.get(year=self.cleaned_data["year"])
		if "top_left_r1_g1" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r1_g1"] != real.top_left_1) and (self.cleaned_data["top_left_r1_g1"] != real.top_left_16):
			raise ValidationError('Invalid Entry: Top Left Round 1 Game 1')
		elif "top_left_r1_g2" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r1_g2"] != real.top_left_8) and (self.cleaned_data["top_left_r1_g2"] != real.top_left_9):
			raise ValidationError('Invalid Entry: Top Left Round 1 Game 2')
		elif "top_left_r1_g3" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r1_g3"] != real.top_left_5) and (self.cleaned_data["top_left_r1_g3"] != real.top_left_12):
			raise ValidationError('Invalid Entry: Top Left Round 1 Game 3')
		elif "top_left_r1_g4" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r1_g4"] != real.top_left_4) and (self.cleaned_data["top_left_r1_g4"] != real.top_left_13):
			raise ValidationError('Invalid Entry: Top Left Round 1 Game 4')
		elif "top_left_r1_g5" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r1_g5"] != real.top_left_6) and (self.cleaned_data["top_left_r1_g5"] != real.top_left_11):
			raise ValidationError('Invalid Entry: Top Left Round 1 Game 5')
		elif "top_left_r1_g6" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r1_g6"] != real.top_left_3) and (self.cleaned_data["top_left_r1_g6"] != real.top_left_14):
			raise ValidationError('Invalid Entry: Top Left Round 1 Game 6')
		elif "top_left_r1_g7" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r1_g7"] != real.top_left_7) and (self.cleaned_data["top_left_r1_g7"] != real.top_left_10):
			raise ValidationError('Invalid Entry: Top Left Round 1 Game 7')
		elif "top_left_r1_g8" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r1_g8"] != real.top_left_2) and (self.cleaned_data["top_left_r1_g8"] != real.top_left_15):
			raise ValidationError('Invalid Entry: Top Left Round 1 Game 8')
		elif "bottom_left_r1_g1" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r1_g1"] != real.bottom_left_1) and (self.cleaned_data["bottom_left_r1_g1"] != real.bottom_left_16):
			raise ValidationError('Invalid Entry: Bottom Left Round 1 Game 1')
		elif "bottom_left_r1_g2" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r1_g2"] != real.bottom_left_8) and (self.cleaned_data["bottom_left_r1_g2"] != real.bottom_left_9):
			raise ValidationError('Invalid Entry: Bottom Left Round 1 Game 2')
		elif "bottom_left_r1_g3" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r1_g3"] != real.bottom_left_5) and (self.cleaned_data["bottom_left_r1_g3"] != real.bottom_left_12):
			raise ValidationError('Invalid Entry: Bottom Left Round 1 Game 3')
		elif "bottom_left_r1_g4" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r1_g4"] != real.bottom_left_4) and (self.cleaned_data["bottom_left_r1_g4"] != real.bottom_left_13):
			raise ValidationError('Invalid Entry: Bottom Left Round 1 Game 4')
		elif "bottom_left_r1_g5" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r1_g5"] != real.bottom_left_6) and (self.cleaned_data["bottom_left_r1_g5"] != real.bottom_left_11):
			raise ValidationError('Invalid Entry: Bottom Left Round 1 Game 5')
		elif "bottom_left_r1_g6" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r1_g6"] != real.bottom_left_3) and (self.cleaned_data["bottom_left_r1_g6"] != real.bottom_left_14):
			raise ValidationError('Invalid Entry: Bottom Left Round 1 Game 6')
		elif "bottom_left_r1_g7" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r1_g7"] != real.bottom_left_7) and (self.cleaned_data["bottom_left_r1_g7"] != real.bottom_left_10):
			raise ValidationError('Invalid Entry: Bottom Left Round 1 Game 7')
		elif "bottom_left_r1_g8" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r1_g8"] != real.bottom_left_2) and (self.cleaned_data["bottom_left_r1_g8"] != real.bottom_left_15):
			raise ValidationError('Invalid Entry: Bottom Left Round 1 Game 8')
		elif "top_right_r1_g1" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r1_g1"] != real.top_right_1) and (self.cleaned_data["top_right_r1_g1"] != real.top_right_16):
			raise ValidationError('Invalid Entry: Top Right Round 1 Game 1')
		elif "top_right_r1_g2" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r1_g2"] != real.top_right_8) and (self.cleaned_data["top_right_r1_g2"] != real.top_right_9):
			raise ValidationError('Invalid Entry: Top Right Round 1 Game 2')
		elif "top_right_r1_g3" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r1_g3"] != real.top_right_5) and (self.cleaned_data["top_right_r1_g3"] != real.top_right_12):
			raise ValidationError('Invalid Entry: Top Right Round 1 Game 3')
		elif "top_right_r1_g4" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r1_g4"] != real.top_right_4) and (self.cleaned_data["top_right_r1_g4"] != real.top_right_13):
			raise ValidationError('Invalid Entry: Top Right Round 1 Game 4')
		elif "top_right_r1_g5" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r1_g5"] != real.top_right_6) and (self.cleaned_data["top_right_r1_g5"] != real.top_right_11):
			raise ValidationError('Invalid Entry: Top Right Round 1 Game 5')
		elif "top_right_r1_g6" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r1_g6"] != real.top_right_3) and (self.cleaned_data["top_right_r1_g6"] != real.top_right_14):
			raise ValidationError('Invalid Entry: Top Right Round 1 Game 6')
		elif "top_right_r1_g7" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r1_g7"] != real.top_right_7) and (self.cleaned_data["top_right_r1_g7"] != real.top_right_10):
			raise ValidationError('Invalid Entry: Top Right Round 1 Game 7')
		elif "top_right_r1_g8" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r1_g8"] != real.top_right_2) and (self.cleaned_data["top_right_r1_g8"] != real.top_right_15):
			raise ValidationError('Invalid Entry: Top Right Round 1 Game 8')
		elif "bottom_right_r1_g1" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r1_g1"] != real.bottom_right_1) and (self.cleaned_data["bottom_right_r1_g1"] != real.bottom_right_16):
			raise ValidationError('Invalid Entry: Bottom Right Round 1 Game 1')
		elif "bottom_right_r1_g2" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r1_g2"] != real.bottom_right_8) and (self.cleaned_data["bottom_right_r1_g2"] != real.bottom_right_9):
			raise ValidationError('Invalid Entry: Bottom Right Round 1 Game 2')
		elif "bottom_right_r1_g3" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r1_g3"] != real.bottom_right_5) and (self.cleaned_data["bottom_right_r1_g3"] != real.bottom_right_12):
			raise ValidationError('Invalid Entry: Bottom Right Round 1 Game 3')
		elif "bottom_right_r1_g4" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r1_g4"] != real.bottom_right_4) and (self.cleaned_data["bottom_right_r1_g4"] != real.bottom_right_13):
			raise ValidationError('Invalid Entry: Bottom Right Round 1 Game 4')
		elif "bottom_right_r1_g5" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r1_g5"] != real.bottom_right_6) and (self.cleaned_data["bottom_right_r1_g5"] != real.bottom_right_11):
			raise ValidationError('Invalid Entry: Bottom Right Round 1 Game 5')
		elif "bottom_right_r1_g6" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r1_g6"] != real.bottom_right_3) and (self.cleaned_data["bottom_right_r1_g6"] != real.bottom_right_14):
			raise ValidationError('Invalid Entry: Bottom Right Round 1 Game 6')
		elif "bottom_right_r1_g7" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r1_g7"] != real.bottom_right_7) and (self.cleaned_data["bottom_right_r1_g7"] != real.bottom_right_10):
			raise ValidationError('Invalid Entry: Bottom Right Round 1 Game 7')
		elif "bottom_right_r1_g8" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r1_g8"] != real.bottom_right_2) and (self.cleaned_data["bottom_right_r1_g8"] != real.bottom_right_15):
			raise ValidationError('Invalid Entry: Bottom Right Round 1 Game 8')
		elif "top_left_r2_g1" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r2_g1"] != self.cleaned_data["top_left_r1_g1"]) and (self.cleaned_data["top_left_r2_g1"] != self.cleaned_data["top_left_r1_g2"]):
			raise ValidationError('Invalid Entry: Top Left Round 2 Game 1')
		elif "top_left_r2_g2" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r2_g2"] != self.cleaned_data["top_left_r1_g3"]) and (self.cleaned_data["top_left_r2_g2"] != self.cleaned_data["top_left_r1_g4"]):
			raise ValidationError('Invalid Entry: Top Left Round 2 Game 2')
		elif "top_left_r2_g3" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r2_g3"] != self.cleaned_data["top_left_r1_g5"]) and (self.cleaned_data["top_left_r2_g3"] != self.cleaned_data["top_left_r1_g6"]):
			raise ValidationError('Invalid Entry: Top Left Round 2 Game 3')
		elif "top_left_r2_g4" in self.cleaned_data.keys() and (self.cleaned_data["top_left_r2_g4"] != self.cleaned_data["top_left_r1_g7"]) and (self.cleaned_data["top_left_r2_g4"] != self.cleaned_data["top_left_r1_g8"]):
			raise ValidationError('Invalid Entry: Top Left Round 2 Game 4')
		elif "bottom_left_r2_g1" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r2_g1"] != self.cleaned_data["bottom_left_r1_g1"]) and (self.cleaned_data["bottom_left_r2_g1"] != self.cleaned_data["bottom_left_r1_g2"]):
			raise ValidationError('Invalid Entry: Bottom Left Round 2 Game 1')
		elif "bottom_left_r2_g2" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r2_g2"] != self.cleaned_data["bottom_left_r1_g3"]) and (self.cleaned_data["bottom_left_r2_g2"] != self.cleaned_data["bottom_left_r1_g4"]):
			raise ValidationError('Invalid Entry: Bottom Left Round 2 Game 2')
		elif "bottom_left_r2_g3" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r2_g3"] != self.cleaned_data["bottom_left_r1_g5"]) and (self.cleaned_data["bottom_left_r2_g3"] != self.cleaned_data["bottom_left_r1_g6"]):
			raise ValidationError('Invalid Entry: Bottom Left Round 2 Game 3')
		elif "bottom_left_r2_g4" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_r2_g4"] != self.cleaned_data["bottom_left_r1_g7"]) and (self.cleaned_data["bottom_left_r2_g4"] != self.cleaned_data["bottom_left_r1_g8"]):
			raise ValidationError('Invalid Entry: Bottom Left Round 2 Game 4')
		elif "top_right_r2_g1" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r2_g1"] != self.cleaned_data["top_right_r1_g1"]) and (self.cleaned_data["top_right_r2_g1"] != self.cleaned_data["top_right_r1_g2"]):
			raise ValidationError('Invalid Entry: Top Right Round 2 Game 1')
		elif "top_right_r2_g2" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r2_g2"] != self.cleaned_data["top_right_r1_g3"]) and (self.cleaned_data["top_right_r2_g2"] != self.cleaned_data["top_right_r1_g4"]):
			raise ValidationError('Invalid Entry: Top Right Round 2 Game 2')
		elif "top_right_r2_g3" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r2_g3"] != self.cleaned_data["top_right_r1_g5"]) and (self.cleaned_data["top_right_r2_g3"] != self.cleaned_data["top_right_r1_g6"]):
			raise ValidationError('Invalid Entry: Top Right Round 2 Game 3')
		elif "top_right_r2_g4" in self.cleaned_data.keys() and (self.cleaned_data["top_right_r2_g4"] != self.cleaned_data["top_right_r1_g7"]) and (self.cleaned_data["top_right_r2_g4"] != self.cleaned_data["top_right_r1_g8"]):
			raise ValidationError('Invalid Entry: Top Right Round 2 Game 4')
		elif "bottom_right_r2_g1" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r2_g1"] != self.cleaned_data["bottom_right_r1_g1"]) and (self.cleaned_data["bottom_right_r2_g1"] != self.cleaned_data["bottom_right_r1_g2"]):
			raise ValidationError('Invalid Entry: Bottom Right Round 2 Game 1')
		elif "bottom_right_r2_g2" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r2_g2"] != self.cleaned_data["bottom_right_r1_g3"]) and (self.cleaned_data["bottom_right_r2_g2"] != self.cleaned_data["bottom_right_r1_g4"]):
			raise ValidationError('Invalid Entry: Bottom Right Round 2 Game 2')
		elif "bottom_right_r2_g3" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r2_g3"] != self.cleaned_data["bottom_right_r1_g5"]) and (self.cleaned_data["bottom_right_r2_g3"] != self.cleaned_data["bottom_right_r1_g6"]):
			raise ValidationError('Invalid Entry: Bottom Right Round 2 Game 3')
		elif "bottom_right_r2_g4" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_r2_g4"] != self.cleaned_data["bottom_right_r1_g7"]) and (self.cleaned_data["bottom_right_r2_g4"] != self.cleaned_data["bottom_right_r1_g8"]):
			raise ValidationError('Invalid Entry: Bottom Right Round 2 Game 4')
		elif "top_left_ss_g1" in self.cleaned_data.keys() and (self.cleaned_data["top_left_ss_g1"] != self.cleaned_data["top_left_r2_g1"]) and (self.cleaned_data["top_left_ss_g1"] != self.cleaned_data["top_left_r2_g2"]):
			raise ValidationError('Invalid Entry: Top Left Round Sweet 16 Game 1')
		elif "top_left_ss_g2" in self.cleaned_data.keys() and (self.cleaned_data["top_left_ss_g2"] != self.cleaned_data["top_left_r2_g3"]) and (self.cleaned_data["top_left_ss_g2"] != self.cleaned_data["top_left_r2_g4"]):
			raise ValidationError('Invalid Entry: Top Left Round Sweet 16 Game 2')
		elif "bottom_left_ss_g1" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_ss_g1"] != self.cleaned_data["bottom_left_r2_g1"]) and (self.cleaned_data["bottom_left_ss_g1"] != self.cleaned_data["bottom_left_r2_g2"]):
			raise ValidationError('Invalid Entry: Bottom Left Round Sweet 16 Game 1')
		elif "bottom_left_ss_g2" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_ss_g2"] != self.cleaned_data["bottom_left_r2_g3"]) and (self.cleaned_data["bottom_left_ss_g2"] != self.cleaned_data["bottom_left_r2_g4"]):
			raise ValidationError('Invalid Entry: Bottom Left Round Sweet 16 Game 2')
		elif "top_right_ss_g1" in self.cleaned_data.keys() and (self.cleaned_data["top_right_ss_g1"] != self.cleaned_data["top_right_r2_g1"]) and (self.cleaned_data["top_right_ss_g1"] != self.cleaned_data["top_right_r2_g2"]):
			raise ValidationError('Invalid Entry: Top Right Round Sweet 16 Game 1')
		elif "top_right_ss_g2" in self.cleaned_data.keys() and (self.cleaned_data["top_right_ss_g2"] != self.cleaned_data["top_right_r2_g3"]) and (self.cleaned_data["top_right_ss_g2"] != self.cleaned_data["top_right_r2_g4"]):
			raise ValidationError('Invalid Entry: Top Right Round Sweet 16 Game 2')
		elif "bottom_right_ss_g1" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_ss_g1"] != self.cleaned_data["bottom_right_r2_g1"]) and (self.cleaned_data["bottom_right_ss_g1"] != self.cleaned_data["bottom_right_r2_g2"]):
			raise ValidationError('Invalid Entry: Bottom Right Round Sweet 16 Game 1')
		elif "bottom_right_ss_g2" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_ss_g2"] != self.cleaned_data["bottom_right_r2_g3"]) and (self.cleaned_data["bottom_right_ss_g2"] != self.cleaned_data["bottom_right_r2_g4"]):
			raise ValidationError('Invalid Entry: Bottom Right Round Sweet 16 Game 2')
		elif "top_left_ee" in self.cleaned_data.keys() and (self.cleaned_data["top_left_ee"] != self.cleaned_data["top_left_ss_g1"]) and (self.cleaned_data["top_left_ee"] != self.cleaned_data["top_left_ss_g2"]):
			raise ValidationError('Invalid Entry: Top Left Elite Eight')
		elif "bottom_left_ee" in self.cleaned_data.keys() and (self.cleaned_data["bottom_left_ee"] != self.cleaned_data["bottom_left_ss_g1"]) and (self.cleaned_data["bottom_left_ee"] != self.cleaned_data["bottom_left_ss_g2"]):
			raise ValidationError('Invalid Entry: Bottom Left Elite Eight')
		elif "top_right_ee" in self.cleaned_data.keys() and (self.cleaned_data["top_right_ee"] != self.cleaned_data["top_right_ss_g1"]) and (self.cleaned_data["top_right_ee"] != self.cleaned_data["top_right_ss_g2"]):
			raise ValidationError('Invalid Entry: Top Right Elite Eight')
		elif "bottom_right_ee" in self.cleaned_data.keys() and (self.cleaned_data["bottom_right_ee"] != self.cleaned_data["bottom_right_ss_g1"]) and (self.cleaned_data["bottom_right_ee"] != self.cleaned_data["bottom_right_ss_g2"]):
			raise ValidationError('Invalid Entry: Bottom Right Elite Eight')
		elif "ff_left" in self.cleaned_data.keys() and (self.cleaned_data["ff_left"] != self.cleaned_data["top_left_ee"]) and (self.cleaned_data["ff_left"] != self.cleaned_data["bottom_left_ee"]) and (self.cleaned_data["ff_left"] != self.cleaned_data["top_right_ee"]) and (self.cleaned_data["ff_left"] != self.cleaned_data["bottom_right_ee"]):
			raise ValidationError('Invalid Entry: Final Four Left')
		elif "ff_right" in self.cleaned_data.keys() and (self.cleaned_data["ff_right"] != self.cleaned_data["top_left_ee"]) and (self.cleaned_data["ff_right"] != self.cleaned_data["bottom_left_ee"]) and (self.cleaned_data["ff_right"] != self.cleaned_data["top_right_ee"]) and (self.cleaned_data["ff_right"] != self.cleaned_data["bottom_right_ee"]):
			raise ValidationError('Invalid Entry: Final Four Right')
		elif "championship" in self.cleaned_data.keys() and (self.cleaned_data["championship"] != self.cleaned_data["ff_left"]) and (self.cleaned_data["championship"] != self.cleaned_data["ff_right"]):
			raise ValidationError('Invalid Entry: Championship')
