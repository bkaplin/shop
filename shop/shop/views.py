from django.shortcuts import render, render_to_response

def main(request):
	return render(request, 'main.html')

def contact(request):
	return render(request, 'contact.html')
