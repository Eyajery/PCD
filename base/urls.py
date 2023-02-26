from django.urls import path
from . import views

urlpatterns = [
    path('activitée/', views.activitée,name='activitée'),
    path('invite/', views.invite,name='invite'),
    path('statistique/', views.statistique,name='statistique'),
    path('lobby/', views.lobby,name='lobby'),
    path('', views.menu),
    path('room/', views.room),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]