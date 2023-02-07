from django.shortcuts import render
import aiohttp

async def inicio(request, pagina=1):

    url = f'https://dadosabertos.camara.leg.br/api/v2/proposicoes?itens=15&pagina={pagina}&ordem=ASC&ordenarPor=id'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            pecs = await response.json()
        for pec in pecs['dados']:
            async with session.get(pec['uri']) as response: 
                pec['proposicao'] = await response.json()
        
    context = {'pecs': pecs, 'pagina': pagina}

    return render(request, 'index.html', context)

async def detalhes(request, pec):

    url = f'https://dadosabertos.camara.leg.br/api/v2/proposicoes/{pec}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            detalhes = await response.json()

    context = {'pec': pec, 'detalhes': detalhes}

    return render(request, 'detalhes.html', context)