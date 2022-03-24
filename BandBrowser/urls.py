from django.urls import path
from BandBrowser import views

app_name = 'BandBrowser'

urlpatterns = [
    path('', views.index, name='index'),

    path('myBandPage/',views.myBandPage, name='myBandPage'),

    path('bandInfoPage/',views.bandInfoPage, name='bandInfoPage'),
    path('updateBandInfo/',views.updateBandInfo, name='updateBandInfo'),
    path('createBandPage/',views.createBandPage, name='createBandPage'),
    path('createBand/',views.createBand, name ='createBand'),

    path('createPostPage/',views.createPostPage, name='createPostPage'),
    path('createBandPost/',views.createBandPost, name='createBandPost'),
    path('createUserPost/',views.createUserPost, name='createUserPost'),

    path('accountPage/',views.accountPage, name='accountPage'),
    path('deleteUserAccount/',views.deleteUserAccount, name='deleteUserAccount'),
    path('updateUserAccount/',views.updateUserAccount, name='updateUserAccount'),
    path('createAccountPage/',views.createAccountPage, name='createAccountPage'),

    path('register/',views.registerUser, name='register'),
    path('loginPage/',views.loginPage, name='loginPage'),
    path('login/',views.userLogin, name='login'),
    path('logout/',views.logoutUser, name='logout'),
]