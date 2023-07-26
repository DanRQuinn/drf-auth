from django.urls import path
from .views import BandsList, BandsDetail

urlpatterns = [
    path('', BandsList.as_view(), name='bands_list'),
    path('<int:pk>/', BandsDetail.as_view(), name='bands_detail'),
]


