from django.shortcuts import render
from django.http import HttpResponse
from studenci.models import Miasto, Uczelnia


def index(request):
    return HttpResponse("Witaj w aplikacji Studenci!")
    # return render(request, 'pizza/index.html')


def miasta(request):

    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        kod = request.POST.get('kod')
        #print(nazwa)
        #print(kod)
        m = Miasto(nazwa=nazwa, kod=kod)
        m.save()

    miasta= Miasto.objects.all()
    kontekst = {
        'miasta': miasta
    }
    return render(request, 'studenci/miasta.html', kontekst)

def uczelnia(request):

    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        #print(nazwa)
        #print(kod)
        u = Uczelnia(nazwa=nazwa)
        u.save()

    uczelnia= Uczelnia.objects.all()
    kontekst = {
        'uczelnia': uczelnia
    }
    return render(request, 'studenci/uczelnia.html', kontekst)