from .models import Gallery, Reservation, MenuItem
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

def home(request):
    return render(request, 'website/index.html')

def menu(request):
    menus = MenuItem.objects.all().order_by('-created_at')
    return render(request, 'website/menu.html', {'menus': menus})

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def gallery(request):
    images_list = Gallery.objects.all().order_by('title')

    paginator = Paginator(images_list, 12)  # 👈 10 images per page
    page_number = request.GET.get('page')
    images = paginator.get_page(page_number)

    return render(request, 'website/gallery.html', {'images': images})

def reservation_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        guests = request.POST.get("guests")

        Reservation.objects.create(
            name=name,
            phone=phone,
            date=date,
            time=time,
            guests=guests
        )

        return redirect('reservation_success')

    return render(request, 'website/reservation.html')

def reservation_success(request):
    reservation = Reservation.objects.latest('id')  # last booking

    return render(request, 'website/success.html', {
        'reservation': reservation
    })