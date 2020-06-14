from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'omikuji/index.html')


def result(request):
    return render(request, 'omikuji/result.html')