import datetime
from django.shortcuts import redirect, render
from django.views import View
from pytube import YouTube
from .utils import video_id
from .models import DownloadRequest

class Downloader(View):
    def get(self, request):
        return render(request, template_name='index.htm')

    def post(self, request):
        
        id = video_id(request.POST.get('link'))

        if id:
            return render(request=request,
                          template_name='download.htm',
                          context={'id' : id},
                          status=200
                        )
        else:
            return render(request=request, 
                          template_name='index.htm',
                          context={'message': 'Entered URL is not valid!'}, 
                          status=400
                        )

class Audio(View):
    def get(self, request, id):
        link = 'https://youtube.com/watch?v=' + id
        video = YouTube(link)

        dt = str(datetime.datetime.now()).replace(' ', '_')
        name = id + '_' + dt + '.mp3'

        audio = video.streams.get_audio_only()
        audio.download(output_path="media/audio/", filename=name)
        audio_url = '/media/audio/' + name

        DownloadRequest.objects.create(
            link=link, video_id=id, file_type='A', address=audio_url,
            expire_time=datetime.datetime.now() + datetime.timedelta(hours=1)
        )

        return redirect(to=audio_url)
        

class LowQualityVideo(View):
    def get(self, request, id):
        link = 'https://youtube.com/watch?v=' + id
        video = YouTube(link)

        dt = str(datetime.datetime.now()).replace(' ', '_')
        name = id + '_' + dt + '.mkv'

        low_quality = video.streams.get_lowest_resolution()
        low_quality.download(output_path="media/low/", filename=name)
        video_url = '/media/low/' + name

        DownloadRequest.objects.create(
            link=link, video_id=id, file_type='L', address=video_url,
            expire_time=datetime.datetime.now() + datetime.timedelta(hours=1)
        )   
         

        return redirect(video_url)


class HighQualityVideo(View):
    def get(self, request, id):
        link = 'https://youtube.com/watch?v=' + id
        video = YouTube(link)

        dt = str(datetime.datetime.now()).replace(' ', '_')
        name = id + '_' + dt + '.mkv'

        high_quality = video.streams.get_highest_resolution()
        high_quality.download(output_path="media/high/", filename=name, )
        video_url = '/media/high/' + name
       
        DownloadRequest.objects.create(
            link=link, video_id=id, file_type='H', address=video_url,
            expire_time=datetime.datetime.now() + datetime.timedelta(hours=1)
        )
        return redirect(video_url)
