#from django.urls import path
#from . import consumers

#websocket_urlpatterns = [
    #path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
#]


from os import path
from django.urls import re_path
from chat import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    path('ws/chat/room_name/', consumers.ImageConsumer.as_asgi()),
]
