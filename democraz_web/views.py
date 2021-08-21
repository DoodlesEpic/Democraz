from django.shortcuts import render
import requests


def inicio(request, pagina=1):

    url = f'https://dadosabertos.camara.leg.br/api/v2/proposicoes?itens=15&pagina={pagina}&ordem=ASC&ordenarPor=id'
    pecs = requests.get(url).json()

    for pec in pecs['dados']:
        pec['proposicao'] = requests.get(pec['uri']).json()

    context = {'pecs': pecs, 'pagina': pagina}

    return render(request, 'index.html', context)
