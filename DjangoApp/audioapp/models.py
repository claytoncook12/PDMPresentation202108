# DjangoApp/audioapp/models.py

from django.db import models

class Audio(models.Model):
    title = models.CharField('Audio File Title', max_length=50)
    audio_file = models.FileField(upload_to="audioapp/", verbose_name="Audio MP3 file")