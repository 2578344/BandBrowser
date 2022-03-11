from django.urls import path
from BandBrowser import views

app_name = 'BandBrowser'

urlpatterns = [
    path('', views.index, name='index'),
    path('myBandPage/',views.myBandPage, name='myBandPage'),

    
]