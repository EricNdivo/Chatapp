import os
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from .consumers import ImageConsumer
def chat_room(request, room_name):
    return render(request, 'chat/chat.html', {'room_name': room_name})

def home(request):
    return render(request, 'home.html')


def chat(request):
    return render(request, 'chat/chat.html')


def help(request):
    print(request.user)
    return render(request, 'help.html')

def send_image(request):
    # Replace 'path/to/your/image.jpg' with the actual path to your image file
    image_path = 'path/to/your/image.jpg'
    consumer = ImageConsumer()
    consumer.send_image(image_path)

    return render(request, 'image_sent.html')


def pdf(request):
    print(request.user)
    pdf_path =  os.path(pdf_file)
    