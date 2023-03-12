import io
from django.http import FileResponse, HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'lab/index.html')
