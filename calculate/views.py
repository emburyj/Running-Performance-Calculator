from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from calculate.utils import Convert, VDOT
from calculate.forms import *

def input_view(request):
    if request.method == "POST":
        pass
    else:
        form_mile = {'Mile': time_input_form()}
        form_5k = {'5,000m': time_input_form()}
        form_10k = {'10,000m': time_input_form()}
        form_half = {'Half-Marathon': time_input_form()}
        form_marathon = {'Marathon': time_input_form()}
        race_forms = [form_mile, form_5k, form_10k, form_half, form_marathon]

        target_form =  target_race_form()

        context = {'race_forms': race_forms, 'target': target_form}
        return render(request, 'input.html', context)

def output_view(request):

    return render(request, 'output.html', context)