from django.urls import path
from . import views

urlpatterns = [
    # path('', views.join_chat, name='join_chat'),
        path('api/add/', views.register_user, name='register_user'),
    path('api/join-room/', views.join_thread),
]
