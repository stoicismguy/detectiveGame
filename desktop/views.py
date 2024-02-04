from django.shortcuts import render

# Create your views here.


def desktop_view(request):
    return render(request, 'desktop.html')
