from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.templatetags.pytils_translit import slugify

from blog.models import MyBlog


class BlogListView(ListView):
    model = MyBlog

    @staticmethod
    def defget_queryset(request, pk):
        blog_public_list = get_object_or_404(MyBlog, pk=pk)
        if blog_public_list.publication_sign:
            blog_public_list.publication_sign = True
        else:
            blog_public_list.publication_sign = False

        return redirect(reverse('blog:blog_detail'))


class BlogDetailView(DetailView):
    model = MyBlog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = MyBlog
    fields = ('name', 'slug', 'content', 'image', 'date_create', 'publication_sign', 'views')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = MyBlog
    fields = ('name', 'slug', 'content', 'image', 'date_create', 'publication_sign', 'views')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=self.kwargs.get('pk'))


class BlogDeleteView(DeleteView):
    model = MyBlog
    success_url = reverse_lazy('blog:blog_list')
