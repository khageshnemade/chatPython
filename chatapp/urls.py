from django.urls import path
from . import views

urlpatterns = [
    # path('', views.join_chat, name='join_chat'),
        path('api/register/', views.register_user, name='register_user'),
    path('api/join-thread/', views.join_thread),
]
