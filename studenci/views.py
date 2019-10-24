from django.shortcuts import render
from django.http import HttpResponse
from studenci.models import Miasto, Uczelnia
from django.contrib import messages


def index(request):
    return HttpResponse("Witaj w aplikacji Studenci!")
    # return render(request, 'pizza/index.html')


def miasta(request):

    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        kod = request.POST.get('kod')
        #print(nazwa)
        #print(kod)
        if len(nazwa.strip()):
            m = Miasto(nazwa=nazwa, kod=kod)
            m.save()
            messages.success(request, "Dane dodano")
        else:
            messages.error(request, "Błędne dane")




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
        if len(nazwa.strip()):
            u = Uczelnia(nazwa=nazwa)
            u.save()
        messages.success(request, "Dane dodano")
    else:
        messages.error(request, "Błędne dane")



    uczelnia= Uczelnia.objects.all()
    kontekst = {
        'uczelnia': uczelnia
    }
    return render(request, 'studenci/uczelnia.html', kontekst)