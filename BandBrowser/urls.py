from django.urls import path
from BandBrowser import views

app_name = 'BandBrowser'

urlpatterns = [
    path('', views.index, name='index'),
    path('myBandPage/',views.myBandPage, name='myBandPage'),
    path('createBandPage/',views.createBandPage, name='createBandPage'),
    path('createPostPage/',views.createPostPage, name='createPostPage'),
    path('accountPage/',views.accountPage, name='accountPage'),
    path('createAccountPage/',views.createAccountPage, name='createAccountPage'),
]