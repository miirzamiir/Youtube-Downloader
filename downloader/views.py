from datetime import datetime
from django.shortcuts import render
from django.views import View
from pytube import YouTube
from .utils import video_id
class Downloader(View):
    def get(self, request):
        return render(request, template_name='index.htm')

    def post(self, request):
        
        link = request.POST.get('link')
        
        id = video_id(link)

        if id:
            video = YouTube(link)
            embeded_url = 'https://youtube.com/embed/' + id

            dt = str(datetime.now()).replace(' ', '_')
            name = id + '_' + dt


            # audio = video.streams.get_audio_only()
            # audio.download(output_path="/media/audio/", filename=name)

            # low_quality = video.streams.get_lowest_resolution()
            # low_quality.download(output_path="/media/low/", filename=name)

            # high_quality = video.streams.get_highest_resolution()
            # high_quality.download(output_path="/media/high/", filename=name)

            return render(request=request,
                          template_name='download.htm',
                          context={'embeded_url': embeded_url},
                          status=200
                        )

        else:
            return render(request=request, 
                          template_name='index.htm',
                          context={'message': 'Entered URL is not valid!'}, 
                          status=400
                        )
