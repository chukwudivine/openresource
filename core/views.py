from django.shortcuts import render, get_object_or_404, redirect
from .models import Resource
from django.core.paginator import Paginator


def home(request):
    searchTerm = request.GET.get('search')
    if searchTerm:
        r = Resource.objects.filter(name__icontains=searchTerm)
    else:
        r = Resource.objects.all()
    paginator = Paginator(r, 8)
    page = request.GET.get('page')
    resource = paginator.get_page(page)
    return render(request, 'home.html', {'searchTerm': searchTerm,'resource': resource})


def upload(request):
    if request.method == 'POST':
        resource = Resource(name = request.POST['name'], content = request.POST['content'])
        resource.save()
        return redirect('home')
    else:
        return render(request, 'upload.html')
    