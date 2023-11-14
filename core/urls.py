from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.doctor, name='doctor'),
    # Added this new path for doctor detail
    path('doctor/<int:pk>/', views.doctorDetails, name='doctor-detail'),
    path('about/', views.about, name='about'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('medicine/', views.medicines, name='medicines'),

    path('medicine/search/', views.medfilterview, name='medfilterview'),

    path('medicinedetail/<int:med_id>/', views.medicinedetail, name='medicinedetail'),

    path('user/', views.userPage, name='user-page'),
    path('room/', views.room_list, name='rooms'),

    path('appointment/', views.appointments, name='appointments'),
    path('room/<int:room_id>/', views.room_details, name='room_details'),


    path('room/<int:room_id>/', views.room_details, name='room_details'),
path('appointment/', views.appointments, name='appointments'),
    path('patient/', views.patients, name='patients'),
    # path('search/', views.searchbar, name='search'),
]
