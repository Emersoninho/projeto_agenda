from django.shortcuts import render
from contact.models import Contact

def create(request):
    context = {
        
    }
    return render(request, 'create.html', context)