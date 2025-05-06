from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(f"Response from {request.path}")

def get_apartment_by_id(request, id):
    return HttpResponse(f"Response from {request.path} with id {id}")