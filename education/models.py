from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class State(models.Model):
    """
	Class to represent education statistics for a particular state
	"""
    GROUP_NAMES = {'mwh':'White',
                  'mhi':'Hispanic',
                  'mbl':'Black',
                  'mas':'Asian',
                  'mam':'Native American',
                  'mtr':'Multiracial',
                  'ecd':'Economically Disadvantaged',
                  'cwd':'Children With Disabilities',
                  'lep':'English Learners'}

    GROUP_NAMES_GRAPH = {'mwh':'White',
                  'mhi':'Hispanic',
                  'mbl':'Black',
                  'mas':'Asian',
                  'mam':'Native \nAmerican',
                  'mtr':'Multiracial',
                  'ecd':'Economically  \nDisadvantaged',
                  'cwd':'Children With\nDisabilities',
                  'lep':'English  \nLearners'}

    state = models.CharField(max_length=2)
    all_cohort = models.IntegerField(validators=[MinValueValidator(0)])
    mam_cohort = models.IntegerField(validators=[MinValueValidator(0)])
    mas_cohort = models.IntegerField(validators=[MinValueValidator(0)])
    mbl_cohort = models.IntegerField(validators=[MinValueValidator(0)])
    mhi_cohort = models.IntegerField(validators=[MinValueValidator(0)])
    mtr_cohort = models.IntegerField(validators=[MinValueValidator(0)])
    mwh_cohort = models.IntegerField(validators=[MinValueValidator(0)])
    cwd_cohort = models.IntegerField(validators=[MinValueValidator(0)])
    ecd_cohort = models.IntegerField(validators=[MinValueValidator(0)])
    lep_cohort = models.IntegerField(validators=[MinValueValidator(0)])
    num_schools = models.IntegerField(validators=[MinValueValidator(0)])
    all_rate = models.DecimalField(max_digits=5,decimal_places=4,validators=[MinValueValidator(0),MaxValueValidator(1)])
    mam_rate = models.DecimalField(null=True,max_digits=5,decimal_places=4,validators=[MinValueValidator(0),MaxValueValidator(1)])
    mas_rate = models.DecimalField(null=True,max_digits=5,decimal_places=4,validators=[MinValueValidator(0),MaxValueValidator(1)])
    mbl_rate = models.DecimalField(null=True,max_digits=5,decimal_places=4,validators=[MinValueValidator(0),MaxValueValidator(1)])
    mhi_rate = models.DecimalField(null=True,max_digits=5,decimal_places=4,validators=[MinValueValidator(0),MaxValueValidator(1)])
    mtr_rate = models.DecimalField(null=True,max_digits=5,decimal_places=4,validators=[MinValueValidator(0),MaxValueValidator(1)])
    mwh_rate = models.DecimalField(null=True,max_digits=5,decimal_places=4,validators=[MinValueValidator(0),MaxValueValidator(1)])
    cwd_rate = models.DecimalField(null=True,max_digits=5,decimal_places=4,validators=[MinValueValidator(0),MaxValueValidator(1)])
    ecd_rate = models.DecimalField(null=True,max_digits=5,decimal_places=4,validators=[MinValueValidator(0),MaxValueValidator(1)])
    lep_rate = models.DecimalField(null=True,max_digits=5,decimal_places=4,validators=[MinValueValidator(0),MaxValueValidator(1)])
