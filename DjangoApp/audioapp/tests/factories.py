# DjangoApp/audioapp/tests/factories.py

from django.conf import settings

import factory
from pathlib import Path
from audioapp import models

class AudioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Audio
    
    title = "Test Title"
    audio_file = str(Path(settings.BASE_DIR) / "audioapp" / "fixtures" / "audioapp" / "test1.mp3")