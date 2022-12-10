from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("tickets.urls")),
    path('accounts/', include("accounts.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Yonna Forex Bureau - IT Help-Desk Admin"
admin.site.site_title = "IT Help-Desk Admin Portal"
admin.site.index_title = "Welcome to IT Help-Desk Portal"
