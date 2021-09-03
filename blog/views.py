from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class PostList(ListView):
    
    queryset = Post.objects.published()
    paginate_by = 5

class PostDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post.objects.published(), slug=slug)
    

