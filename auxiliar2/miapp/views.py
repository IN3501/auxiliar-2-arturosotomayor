from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def pestaña(request):
	return render(request, 'miapp/pestaña.html')

def TicsDesafio1(request):
	return render(request, 'miapp/TicsDesafio1.html')