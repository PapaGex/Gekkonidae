from django.urls import path

from geckos.views import GeckoList, GeckoDetail

urlpatterns = [
    path('', GeckoList.as_view(), name='gecko_list'),
    path('<int:pk>/', GeckoDetail.as_view(), name='species_details'),
]