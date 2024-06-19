from articles.engine import Article
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product


class ProductDitailView(DetailView):
    model = Product


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)

        if self.request.method == 'POST':
            context['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if form.is_valid and formset.is_valid:
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=formset))


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["latest_articles"] = Article.objects.all()
        return context
