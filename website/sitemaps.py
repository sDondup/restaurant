from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.contrib.sites.models import Site

class StaticViewSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return [
            'home',
            'menu',
            'about',
            'contact',
            'gallery',
            'reservation',
            'reservation_success',
        ]

    def location(self, item):
        return reverse(item)

    def get_urls(self, site=None, **kwargs):
        site = Site.objects.get_current()
        self.domain = site.domain
        return super().get_urls(site=site, **kwargs)