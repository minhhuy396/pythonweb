from django.shortcuts import render
from .models import Phongban, Nhanvien, Dean, Phancong, Thannhan


def index(request):
    context = {
        'phongban': Phongban.objects.all(),
        'nhanvien': Nhanvien.objects.all(),
        'dean': Dean.objects.all(),
        'phancong': Phancong.objects.all(),
        'thannhan': Thannhan.objects.all(),
    }
    return render(request, 'index.html', context)