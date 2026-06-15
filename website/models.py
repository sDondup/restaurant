from django.db import models

# index page model
class Home(models.Model):
    title_eng = models.CharField(max_length=255)
    title_nl = models.CharField(max_length=255)

    description_eng = models.TextField()
    description_nl = models.TextField()

    video = models.FileField(upload_to='home/', blank=True, null=True)

    def __str__(self):
        return self.title_eng

class OurStory(models.Model):
    title_eng = models.CharField(max_length=255)
    title_nl = models.CharField(max_length=255)

    content_eng = models.TextField()
    content_nl = models.TextField()

    image = models.ImageField(upload_to='home/')

    def __str__(self):
        return self.title_eng

class WhyChooseUs(models.Model):

    title_eng = models.CharField(max_length=255, default="Why Choose Us")
    title_nl = models.CharField(max_length=255, default="Why Choose Us")

    icon = models.CharField(max_length=100, default="fa-star")

    content_eng = models.TextField()
    content_nl = models.TextField()

    def __str__(self):
        return self.title_eng

#gallery page model
class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} | {self.date} | {self.time} | {self.guests} Guests"

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='menu/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class MenuCard(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('NL', 'NL'),
    ]

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='menu/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_language_display()} - {self.title}"

class Contact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    open_hours = models.CharField(max_length=255)

    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    location = models.URLField(blank=True)

    def __str__(self):
        return self.phone

class AboutUs(models.Model):
    title_eng = models.CharField(max_length=255)
    title_nl = models.CharField(max_length=255)

    content_eng = models.TextField()
    content_nl = models.TextField()

    def __str__(self):
        return self.title_eng

class FounderSection(models.Model):
    title_eng = models.CharField(max_length=255)
    title_nl = models.CharField(max_length=255)

    content_eng = models.TextField()
    content_nl = models.TextField()

    signature_eng = models.CharField(max_length=255)
    signature_nl = models.CharField(max_length=255)

    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title_eng

class WhoWeAre(models.Model):
    title_eng = models.CharField(max_length=255)
    title_nl = models.CharField(max_length=255)

    content_eng = models.TextField()
    content_nl = models.TextField()

    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title_eng

class Mission(models.Model):
    title_eng = models.CharField(max_length=255)
    title_nl = models.CharField(max_length=255)

    content_eng = models.TextField()
    content_nl = models.TextField()

    def __str__(self):
        return self.title_eng

class Value(models.Model):
    title_eng = models.CharField(max_length=100)
    title_nl = models.CharField(max_length=100)

    content_eng = models.TextField()
    content_nl = models.TextField()

    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title_eng