# DjangoApp/audioapp/tests/test_model.py
import pytest

from audioapp.tests import factories

@pytest.mark.django_db
class TestAudio:
    def test_init(self):
        obj = factories.AudioFactory()
        assert obj.pk == 1, "Should save an instance"

        # Check varing properties about default file
        # Size in bytes
        assert obj.audio_file.size == 270836, "Should be able to check audio file size"