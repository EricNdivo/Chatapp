import os
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from .consumers import ImageConsumer
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from chat.models import UserProfile

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

#Function to download pdf file(Not priority)
"""def pdf(request):
    print(request.user)
    pdf_path =  os.path(pdf_file)"""
    
    
#Function to view active users
"""def users(request):
    print(request.user)"""
    
#Fuction to add a profile picture
"""def profilepicture(request):
    print(request.user)"""
  
  
def download_profile_picture(request, user_id):
    user_profile = get_object_or_404(UserProfile, id=user_id)
    profile_picture_path = user_profile.profile_picture.path
    with open(profile_picture_path, 'rb') as picture_file:
        response = FileResponse(picture_file)
        response['Content-Type'] = 'image/jpeg'
        response['Content-Disposition'] = f'attachment; filename="{user_profile.profile_picture.name}"'

        return response
  
