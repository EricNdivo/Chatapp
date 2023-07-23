from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('room/<str:room_name>/', views.chat_room, name='chat_room'),
    path('', views.home, name='home'),
    path('chat',views.chat,name='chat'),
    path('help',views.help,name='help')
    
]
