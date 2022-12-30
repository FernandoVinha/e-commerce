from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import ReproductionStage,Pig,Birth
from datetime import datetime
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework import permissions
from farm_pig.serializers import PigSerializer , BirthSerializer

# Create your views here.
class PigViewSet(viewsets.ModelViewSet):
    queryset = Pig.objects.all()
    serializer_class = PigSerializer

class  BirthViewSet(viewsets.ModelViewSet):
    queryset =  Birth.objects.all()
    serializer_class = BirthSerializer

def farm(request):
    return render(request, 'farm.html')

def pig (request):
    _pig =  Pig.objects.all()
    print(_pig)

def birth(request):
    x = Birth.objects.all()
    
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    _live_born = []
    #_stillbirth = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.live_born for i in x if i.date.month == mes and i.date.year == ano])
        #z = sum([i.stillbirth for i in x if i.date.month == mes and i.date.year == ano])
        labels.append(meses[mes-1])
        _live_born.append(y)
        #_stillbirth.append(z)
        cont += 1

    data_json = {'live_born': _live_born[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)