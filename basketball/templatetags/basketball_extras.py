from django import template

register = template.Library()

CONF_NAMES = {
    'AE': 'America East',
	"AAC": 'American Athletic',
	"A10": 'Atlantic 10',
	"ACC": 'Atlantic Coast',
	"AS": 'Atlantic Sun',
	"BIG12": 'Big 12',
	"BIGEAST": 'Big East',
	"BIGSKY": 'Big Sky',
	"BIGSOUTH": 'Big South',
	"BIG10": 'Big Ten',
	"BIGWEST": 'Big West',
	"COLONIAL": 'Colonial',
	"CUSA": 'Conference USA',
	"HORIZON": 'Horizon',
	"IVY": 'Ivy',
	"MAAC": 'Metro Atlantic Athletic',
	"MEAC": 'Mid Eastern Athletic',
	"MAC": 'Mid-American',
	"MVC": 'Missouri Valley',
	"MWC": 'Mountain West',
	"NE": 'Northeast',
	"OVC": 'Ohio Valley',
	"PAC12": 'Pacific 12',
	"PATRIOT": 'Patriot League',
	"SEC": 'Southeastern',
	"SOUTHERN": 'Southern',
	"SOUTHLAND": 'Southland',
	"SWAC": 'Southwestern Athletic',
	"SUMMIT": 'Summit League',
	"SUNBELT": 'Sun Belt',
	"WCC": 'West Coast',
	"WAC": 'Western Athletic',
}

@register.filter
def long_conf(value):
    return CONF_NAMES[value]
