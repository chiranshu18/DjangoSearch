from django.shortcuts import render

from django.shortcuts import render

from .models import Contact


def index(request):
    search_term = request.POST.get('search_term', '')
    contacts = Contact.objects.filter(name__icontains=search_term)
    return render(request, 'base.html', {'contacts': contacts})
    # return render(request, 'base.html')