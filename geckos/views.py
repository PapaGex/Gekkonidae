from rest_framework import generics
from rest_framework import viewsets
from .models import Gecko
from django.http import JsonResponse
from .serializers import GeckoSerializer

class GeckoList(generics.ListAPIView):
    queryset = Gecko.objects.all()
    serializer_class = GeckoSerializer
def gecko_list(request):
    geckos = Gecko.objects.all()
    data = {
        'geckos': list(geckos.values())
        }
    return JsonResponse(data)

class GeckoViewSet(viewsets.ModelViewSet):
    queryset = Gecko.objects.all()
    serializer_class = GeckoSerializer


class GeckoDetail(generics.RetrieveAPIView):
    queryset = Gecko.objects.all()
    serializer_class = GeckoSerializer

def species_details(request, pk):
    gecko = Gecko.objects.get(pk=pk)
    data = {
        'name': gecko.name,
        'genus': gecko.genus,
        'species': gecko.species,
        'description': gecko.description,
        'discovered': gecko.discovered,
        'habitat': gecko.habitat,
        'snout_to_vent': gecko.snout_to_vent,
        'lifespan': gecko.lifespan,
        'species_range': gecko.species_range,
    }
    return JsonResponse(data)

