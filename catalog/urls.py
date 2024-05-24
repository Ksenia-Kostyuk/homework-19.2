from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import base, product_detail, contact

app_name = CatalogConfig.name

urlpatterns = [
    path("", base, name="index"),
    path("contact/", contact, name="contact"),
    path("catalog/<int:pk>/", product_detail, name="product_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
