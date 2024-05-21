from django.shortcuts import render,redirect
from pytube import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        
        link=request.POST['link']   # getting link from frontend
        video=YouTube(link)

        stream = video.streams.get_lowest_resolution() #setting video resolution

        stream.download()  # downloads video

        return render(request,'index.html')

    return render(request, 'index.html')