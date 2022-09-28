from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from utils import Convert, VDOT
# Create your views here.
def input_view(request):
    if request.method == "POST":
        pass
    else:
        context = {}
        return render(request, 'input.html', context)

def output_view(request):

    return render(request, 'output.html', context)