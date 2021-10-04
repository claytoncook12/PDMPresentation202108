# DjangoApp/audioapp/tests/test_views.py
import pytest

from django.test import Client
from django.urls import reverse

from audioapp.tests import factories

@pytest.mark.django_db
class TestDetailViewAudio:
    def test_shows_title(self):
        client = Client()
        
        # Create Audio and Get pk
        obj = factories.AudioFactory()
        pk  = obj.pk

        # Get detail view of audio created above
        response = client.get(reverse("audioapp:detail", args=(pk,)))

        assert response.status_code == 200, "View returns 200 status code"
        assert obj.title in response.content.decode(), "The audioapp.detail view shows the audio.title"