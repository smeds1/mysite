from django import template

register = template.Library()

STATE_NAMES = {
    'AK': 'Alaska',
    'AL': 'Alabama',
	'AR': 'Arkansas',
    'AZ': 'Arizona',
    'BI': 'Bureau of Indian Affairs',
    'CA': 'California',
	'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
	'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
	'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
	'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
	'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
	'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
	'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
	'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
	'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
	'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
	'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
	'WV': 'West Virginia',
    'WY': 'Wyoming',
}

@register.filter
def long_state(value):
    """
    Display a state abbreviation as the full name (e.g. display WA as Washington)
    """
    return STATE_NAMES[value]

@register.filter
def percentage(value):
    """
    Display a decimal as a percentage with one decimal plae
    (e.g. display 0.3942 as 39.4%)
    """
    return format(value,'.1%')
