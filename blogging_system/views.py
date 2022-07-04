from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from . models import Post, Category


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['category'] = category
        return context


class PostListView(ListView):
    context_object_name = 'post'
    template_name = 'post_list.html'
    model = Post


class PostDetailView(DetailView):
    context_object_name = 'post'
    template_name = 'post_detail.html'
    model = Post

