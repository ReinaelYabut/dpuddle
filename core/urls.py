from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.doctor, name='doctor'),
    path('about/', views.about, name='about'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('user/', views.userPage, name='user-page'),
]
