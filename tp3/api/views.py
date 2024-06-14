import requests
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'api/index.html')

def buscar(request):
    query = request.GET.get('provincia')
    url = f'https://apis.datos.gob.ar/georef/api/provincias?nombre={query}&campos=id,nombre,centroide.lat,centroide.lon'
    response = requests.get(url)
    data = response.json()
    provincias = data.get('provincias', [])

    for provincia in provincias:
        detalle_url = f'https://apis.datos.gob.ar/georef/api/provincias/{provincia["id"]}'
        detalle_response = requests.get(detalle_url)
        detalle_data = detalle_response.json().get('provincias', [])
        if detalle_data:
            provincia_detalle = detalle_data[0]
            provincia['poblacion'] = provincia_detalle.get('poblacion', 'Desconocido')
            provincia['superficie'] = provincia_detalle.get('superficie', 'Desconocido')
        else:
            provincia['poblacion'] = 'Desconocido'
            provincia['superficie'] = 'Desconocido'

    return render(request, 'api/resultados.html', {'provincias': provincias})

def autocomplete(request):
    query = request.GET.get('q')
    url = f'https://apis.datos.gob.ar/georef/api/provincias?nombre={query}'
    response = requests.get(url)
    data = response.json()
    provincias = data.get('provincias', [])
    return JsonResponse({'provincias': provincias})
