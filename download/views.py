from django.shortcuts import render, redirect 
from pytube import *
  
def index(request): 
   
    if request.method == 'POST': 
        
        link = request.POST['link']  # getting link from frontend 
        video = YouTube(link) 
  
        stream = video.streams.get_lowest_resolution()  # setting video resolution
          
        # downloads video 
        stream.download() 
  
        return render(request, 'index.html') 
    return render(request, 'index.html')