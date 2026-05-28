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

        # SAVE TO DATABASE
        reservation = Reservation.objects.create(
            name=name,
            phone=phone,
            date=date,
            time=time,
            guests=guests
        )

        # SAVE ID FOR SUCCESS PAGE
        request.session["reservation_id"] = reservation.id

        # WHATSAPP MESSAGE
        whatsapp_message = quote(
            f"🍽 New Reservation Request\n\n"
            f"Name: {name}\n"
            f"Phone: {phone}\n"
            f"Date: {date}\n"
            f"Time: {time}\n"
            f"Guests: {guests}"
        )

        # OWNER NUMBER
        whatsapp_url = (
            f"https://wa.me/32491180010?text={whatsapp_message}"
        )

        # REDIRECT TO WHATSAPP
        return redirect(whatsapp_url)

    return render(request, 'website/reservation.html')

def reservation_success(request):

    reservation_id = request.session.get("reservation_id")

    reservation = Reservation.objects.get(id=reservation_id)

    return render(
        request,
        'website/reservation_success.html',
        {"reservation": reservation}
    )

def reservation_success(request):
    reservation = Reservation.objects.latest('id')  # last booking

    return render(request, 'website/success.html', {
        'reservation': reservation
    })