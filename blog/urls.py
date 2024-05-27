from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="base"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('publication/<int:pk>', BlogListView.defget_queryset(), name='blog_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
