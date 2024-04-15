from django.shortcuts import render


# Create your views here.
def IndexView(request):
    '''esto es una view'''
    return render(request, 'index.html')

