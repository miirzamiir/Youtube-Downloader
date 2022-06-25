from django.db import models
    
class DownloadRequest(models.Model):

    FILE_TYPE_CHOICES = [
        ('A', 'Audio'),
        ('L', 'Low Quality Video'),
        ('H', 'High Quality Video')
    ]

    link = models.CharField(max_length=255)
    video_id = models.CharField(max_length=15)
    requested_at = models.DateTimeField(auto_now=True)
    expire_time = models.DateTimeField()
    file_type = models.CharField(max_length=2, choices=FILE_TYPE_CHOICES)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.video_id + '_' + self.requested_at