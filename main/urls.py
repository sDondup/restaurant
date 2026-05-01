from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

# language switch endpoint (must stay OUTSIDE i18n_patterns)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# all site pages go inside i18n_patterns
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
)

# ✅ ADD THIS LINE
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)