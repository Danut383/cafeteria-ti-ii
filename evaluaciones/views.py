from django.shortcuts import render

def index(request):
    return render(request, 'evaluaciones/index.html')

def cafeteria_norte(request):
    return render(request, 'evaluaciones/cafeteria_norte.html')

def cafeteria_sur(request):
    return render(request, 'evaluaciones/cafeteria_sur.html')
