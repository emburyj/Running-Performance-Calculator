from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from calculate.utils import Convert, VDOT, Predict
from calculate.forms import *
from collections import OrderedDict

def input_view(request):
    std_distances = {'Mile': 1609.34, '5,000m': 5000, '10,000m': 10000, 'Half-Marathon': 21097.5, 'Marathon': 42195}
    if request.method == "POST":
        if 'reset' in request.POST.keys():
            return HttpResponseRedirect("/")
        if 'calculate' in request.POST.keys():
            form = time_input_form(request.POST)
            for dist in std_distances.keys():
                form.fields[f'hr_{dist}'] = form.fields['hours']
                form.fields[f'min_{dist}'] = form.fields['minutes']
                form.fields[f'sec_{dist}'] = form.fields['seconds']
            del(form.fields['hours'])
            del(form.fields['minutes'])
            del(form.fields['seconds'])
            vdot_list = []
            if form.is_valid():
                for dist, meters in std_distances.items():
                    if not form.cleaned_data[f'hr_{dist}']:
                        form.cleaned_data[f'hr_{dist}'] = 0
                    if not form.cleaned_data[f'min_{dist}']:
                        form.cleaned_data[f'min_{dist}'] = 0
                    if not form.cleaned_data[f'sec_{dist}']:
                        form.cleaned_data[f'sec_{dist}'] = 0
                    current_time = [form.cleaned_data[f'hr_{dist}'], form.cleaned_data[f'min_{dist}'], form.cleaned_data[f'sec_{dist}']]
                    if sum(current_time) > 0:
                        t = Convert.time_lst_to_minutes(current_time)
                        vdot_list.append([VDOT.get_vdot(meters, t), dist, t])
                perfs = sorted(vdot_list, key=lambda x: x[0], reverse=True) # sorted (by vdot) list of performances [vdot, str(race distance), decimal distance in meters]
                rank_perf = OrderedDict()
                for i in range(1, len(perfs)+1):
                    rank_perf[i] = [perfs[i-1][1], Convert.time_minutes_to_str(perfs[i-1][2]), round(perfs[i-1][0], 2)]

                target_form = target_race_form(request.POST)
                if target_form.is_valid():
                    if int(target_form.cleaned_data['units']) == 1:
                        target_distance = 1000*Convert.miles_to_km(float(target_form.cleaned_data['distance'])) # convert miles to meters
                        target_units = 'mi'
                    else:
                        target_distance = target_form.cleaned_data['distance']*1000 # convert km to m
                        target_units = 'km'
                    target_grade = target_form.cleaned_data['avg_grade']

                    if len(perfs) != 0 and target_distance != 0:
                        target_dist_str = f"{target_form.cleaned_data['distance']}{target_units} with {target_grade}% average gradient"
                        target_vdot = perfs[0][0]
                        print(f"\ntarget vdot is: {target_vdot};\n target distance is: {int(target_distance)}m;\n target grade is: {target_grade}%;\n")# time predicted: {target_time}")
                        target_time = Predict.performance(target_vdot, float(target_distance), float(target_grade))
                    elif len(perfs) == 0:
                        target_dist_str = "Please enter at least one personal best running time"
                        target_time = ""
                    else:
                        target_dist_str = "Please enter a valid target distance"
                        target_time = ""
                    target_performance = {target_dist_str: target_time}
                else:
                    target_dist_str = "Please enter a valid target distance"
                    target_time = ""
                    target_performance = {target_dist_str: target_time}

                context = {'calculate': True, 'race_forms': form, 'target': target_form, 'rank_perf': rank_perf, 'target_perf': target_performance}
                return render(request, 'input.html', context)

    else:
        race_forms = []
        for dist in std_distances.keys():
            current_form = time_input_form()
            current_form.fields[f"hr_{dist}"] = current_form.fields["hours"]
            del(current_form.fields["hours"])
            current_form.fields[f"min_{dist}"] = current_form.fields["minutes"]
            del(current_form.fields["minutes"])
            current_form.fields[f"sec_{dist}"] = current_form.fields["seconds"]
            del(current_form.fields["seconds"])
            race_forms.append({dist: current_form})

        target_form =  target_race_form()

        context = {'race_forms': race_forms, 'target': target_form}
        return render(request, 'input.html', context)