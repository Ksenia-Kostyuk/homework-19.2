from articles.engine import Article
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDitailView(DetailView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = Article.objects.all()
        return context
