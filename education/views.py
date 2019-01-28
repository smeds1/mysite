from django.shortcuts import render
from django.db.models import Sum, F, FloatField
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import State

def index(request):
    """
	Main index page for the education project. The page displays the premise
	of the project as well a choreopleth of the graduation rates by state.
	"""
    states = State.objects.values("state",value=F("all_rate")).all()

    if states:
        json_data = json.dumps(list(states), cls=DjangoJSONEncoder)
        return render(request, 'education/index.html',{'json_data':json_data})
    else:
        return render(request, 'education/index.html')

def states(request):
    """
	The states page contains a list of all U.S. states and statistics associated
    with each one.
	"""
    return render(request, 'education/states.html', {'states':State.objects.all()})

def demographics(request):
    """
    The deomgraphics page shows the overall number of students in each demographic
    and the national graduation rate for each demographic.
    """
    cohort_sums = State.objects.aggregate(Sum("all_cohort"),Sum("mwh_cohort"),Sum("mbl_cohort"),
            Sum("mas_cohort"),Sum("mhi_cohort"),Sum("mam_cohort"),
            Sum("mtr_cohort"),Sum("ecd_cohort"),Sum("lep_cohort"),
            Sum("cwd_cohort"),Sum("all_cohort"))
    grad_sums = State.objects.annotate(mwh_grad = F("mwh_rate")*F("mwh_cohort"),
            mbl_grad = F("mbl_rate")*F("mbl_cohort"),
            mas_grad = F("mas_rate")*F("mas_cohort"),
            mhi_grad = F("mhi_rate")*F("mhi_cohort"),
            mam_grad = F("mam_rate")*F("mam_cohort"),
            mtr_grad = F("mtr_rate")*F("mtr_cohort"),
            ecd_grad = F("ecd_rate")*F("ecd_cohort"),
            lep_grad = F("lep_rate")*F("lep_cohort"),
            cwd_grad = F("cwd_rate")*F("cwd_cohort"),
            all_grad = F("all_rate")*F("all_cohort")).aggregate(
            Sum("mwh_grad",output_field=FloatField()),
            Sum("mbl_grad",output_field=FloatField()),
            Sum("mas_grad",output_field=FloatField()),
            Sum("mhi_grad",output_field=FloatField()),
            Sum("mam_grad",output_field=FloatField()),
            Sum("mtr_grad",output_field=FloatField()),
            Sum("ecd_grad",output_field=FloatField()),
            Sum("lep_grad",output_field=FloatField()),
            Sum("cwd_grad",output_field=FloatField()),
            Sum("all_grad",output_field=FloatField()))

    context = {}
    demographics_data = []
    if cohort_sums["all_cohort__sum"]:
        for group in ['mwh','mbl','mas','mhi','mam','mtr','ecd','lep','cwd','all']:
            context[group+"_cohort"] = cohort_sums[group+"_cohort__sum"]
            context[group+"_rate"] = grad_sums[group+"_grad__sum"]/cohort_sums[group+"_cohort__sum"]
            if group != 'all':
                demographics_data.append({'group':State.GROUP_NAMES_GRAPH[group],'value':100*cohort_sums[group+"_cohort__sum"]/cohort_sums["all_cohort__sum"]})
        context["json_data"] = json.dumps(demographics_data)
        return render(request, 'education/demographics.html', context)
    else:
        return render(request, 'education/demographics.html')

def state_detail(request, state_abbr):
    """
    The states detail page contains data for the specified U.S. state. A graph
    of the population demographics is displayed.
    """
    try:
        data = State.objects.get(state=state_abbr)
    except State.DoesNotExist:
        message = "No data for state {}".format(state_abbr)
        return render(request, 'education/error.html', {"message": message})

    demographics_data = []
    for group in ['mwh','mbl','mas','mhi','mam','mtr','ecd','lep','cwd']:
        demographics_data.append({'group':State.GROUP_NAMES_GRAPH[group],
                'value':100*getattr(data, group+'_cohort')/data.all_cohort})
    context = {'data':data, 'json_data':json.dumps(demographics_data)}

    return render(request, 'education/state_detail.html',context)

def demographic_detail(request, group):
    """
    The deomgraphic_detail page shows two maps for the chosen demographic: one
    that represents the percentage of the cohort that is in the demographic and
    one that represents the graduation rate for the demographic.
    """
    if not group in State.GROUP_NAMES:
        message = "No such group {}".format(group)
        return render(request, 'education/error.html', {"message": message})

    data = State.objects.exclude(state__in=['BI','DC'])
    population_data = []
    rate_data = []
    for row in data:
        group_cohort = getattr(row, group+'_cohort')
        group_rate = getattr(row, group+'_rate')
        population_data.append({'state':row.state,'value':group_cohort/row.all_cohort})
        rate_data.append({'state':row.state,'value':float(group_rate) if group_rate else None})

    context = {'group':State.GROUP_NAMES[group],
            'json_population_data':json.dumps(population_data),
            'json_rate_data':json.dumps(rate_data)}
    return render(request, 'education/demographic_detail.html',context)

def stats(request):
    return render(request, 'education/stats.html')
