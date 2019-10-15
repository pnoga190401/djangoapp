from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Witaj w studenci!!")
    #return render(request, 'studenci/index.html')





