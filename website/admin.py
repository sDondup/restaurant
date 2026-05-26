from django.contrib import admin
from .models import Gallery, Reservation, MenuItem

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Reservation)
admin.site.register(MenuItem)