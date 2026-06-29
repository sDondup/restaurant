from .models import (
    Home, OurStory, WhyChooseUs, Gallery, Reservation,
    MenuCard, Contact, AboutUs, FounderSection,
    WhoWeAre, Mission, Value, GoogleReview, CustomerReview
)
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from urllib.parse import quote
from django.utils.translation import get_language

def home(request):

    language = get_language()

    home_data = Home.objects.first()
    story = OurStory.objects.first()
    why_items = WhyChooseUs.objects.all()
    contact_info = Contact.objects.first()
    google_review = GoogleReview.objects.first()
    customer_review = CustomerReview.objects.all()[:20]  # latest 6 reviews

    return render(request, 'website/index.html', {
        'language': language,
        'home': home_data,
        'story': story,
        'why_items': why_items,
        'contact_info': contact_info,
        "google_review": google_review,
        'customer_review': customer_review,
    })

def menu(request):

    language = get_language()

    menus = MenuCard.objects.filter(language=language)

    return render(request, 'website/menu.html', {
        'menus': menus,
        'language': language,
    })

def about(request):

    language = get_language()

    context = {
        'language': language,
        'about': AboutUs.objects.first(),
        'founder': FounderSection.objects.first(),
        'who': WhoWeAre.objects.first(),
    }

    return render(request, 'website/aboutus.html', context)

def contact(request):

    contact_info = Contact.objects.first()

    language = get_language()

    display_hours = None

    if contact_info:
        if language == "nl":
            display_hours = contact_info.opening_hours_nl
        else:
            display_hours = contact_info.opening_hours_en

    return render(request, 'website/contact.html', {
        'contact_info': contact_info,
        'display_hours': display_hours
    })

def gallery(request):

    images_list = Gallery.objects.all().order_by('title')

    paginator = Paginator(images_list, 12)
    page_number = request.GET.get('page')

    images = paginator.get_page(page_number)

    return render(request, 'website/gallery.html', {
        'images': images
    })

def reservation_view(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        guests = request.POST.get("guests")
        special_requests = request.POST.get("special_requests")

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
            f"Guests: {guests}\n"
            f"Special Requests: {special_requests or 'None'}"
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