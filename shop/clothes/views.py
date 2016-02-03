from django.shortcuts import render
from clothes.models import Clothes

def all_clothes(request):
	clothes = Clothes.objects.all()
	return render(request, 'clothes/all_clothes.html', {'clothes':clothes})

def detail(request, pk):
	jacket = Clothes.objects.get(id = pk)
	return render(request, 'clothes/detail.html', {'jacket':jacket})
