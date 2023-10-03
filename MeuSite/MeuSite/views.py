from django.shortcuts import render

def homeSec(request):
    return render(request,
        "registro/homeSec.html")