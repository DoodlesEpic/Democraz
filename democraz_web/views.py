from django.shortcuts import render
import requests


def inicio(request):

    url = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes?itens=100&ordem=ASC&ordenarPor=id'
    pecs = requests.get(url).json()

    context = {
        'pecs': pecs,
    }
    return render(request, 'index.html', context)
