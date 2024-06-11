from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDitailView, ContactTemplateView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="index"),
    path("contact/", ContactTemplateView.as_view(), name="contact"),
    path("catalog/<int:pk>/", ProductDitailView.as_view(), name="product_detail"),
    path("catalog/create/", ProductCreateView.as_view(), name="product_create"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
