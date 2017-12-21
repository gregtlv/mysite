from django.shortcuts import render

# Create your views here.

def vera_main(request):
    return render(request, 'vera/vera_main.html', {})
