from django.shortcuts import render
from .models import Gallery
from django.core.paginator import Paginator

def home(request):
    return render(request, 'website/index.html')

def menu(request):
    return render(request, 'website/menu.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def gallery(request):
    images_list = Gallery.objects.all()

    paginator = Paginator(images_list, 12)  # 👈 10 images per page
    page_number = request.GET.get('page')
    images = paginator.get_page(page_number)

    return render(request, 'website/gallery.html', {'images': images})