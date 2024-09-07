# example/views.py
from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

def index(request):
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    context = {
        'now': now
    }

    return render(request, 'index.html', context)