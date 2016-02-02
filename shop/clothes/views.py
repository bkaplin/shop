from django.shortcuts import render
from clothes.models import Clothes

def all_clothes(request):
	clothes = Clothes.objects.all()
	return render(request, 'clothes/all_clothes.html', {'clothes':clothes})
