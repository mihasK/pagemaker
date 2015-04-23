from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def demo(request):
   return render(request, 'demo.html')

def main(request):
   return render(request, 'main.html', {'school':0})
