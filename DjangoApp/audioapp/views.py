# DjangoApp/audioapp/views.py

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Audio

# Create your views here.
def detail(request, pk):

    obj = get_object_or_404(Audio, pk=pk)

    context = {
        "obj": obj,
    }

    return render(request, 'audioapp/detail.html', context)