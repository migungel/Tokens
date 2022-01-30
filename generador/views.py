from django.shortcuts import render
#from django.http import HttpResponse
import random
from time import sleep

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def timer(request):
    return render(request, 'timer.html')

#def timeout(request):
#    cnt=5
#    for x in range(5):
#        cnt -= 1
#        sleep(1)
#    print("60 segundos")
#    return render(request, 'token.html')

def token(request):
    numbers = list('1234567890')
    gtoken = ''
    for n in range(6):
        gtoken += random.choice(numbers)
    
    return render(request, 'token.html', {'token':gtoken})
    #return render(request, 'token.html', {'token':gtoken, 'time':cnt})