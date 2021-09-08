from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Category, Post
# Create your views here.

class PostList(ListView):
    
    queryset = Post.objects.published()
    paginate_by = 5

class PostDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post.objects.published(), slug=slug)
        
    

class CategoryList(ListView):
    paginate_by = 5
    template_name="blog/category_list.html"


    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.all(), slug=slug)
        return category.posts.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category 
        return context