from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Home page!")

def user(request, id):
    return HttpResponse(f"User ID: {id}")
