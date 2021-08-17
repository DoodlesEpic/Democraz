from django.http import HttpResponse


def inicio(request):
    return HttpResponse("Olá, seja bem-vindo ao Democraz.")
