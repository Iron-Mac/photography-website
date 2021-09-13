from django.db import models
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .mixins import AdminAccessMixin, PostFieldsMixin,FormValidMixin ,SuperUserAccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post


# Create your views here.

class PostList(LoginRequiredMixin,SuccessMessageMixin,ListView):
    template_name = 'registration/home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.filter(author=self.request.user)


class PostCreate(LoginRequiredMixin,PostFieldsMixin,FormValidMixin,SuccessMessageMixin,CreateView):
    model = Post
    template_name = "registration/post-create-update.html"
    success_url = reverse_lazy('account:create_post')
    success_message = "پست شما با موفقیت ساخته شد"

class PostUpdate(LoginRequiredMixin,PostFieldsMixin,FormValidMixin,SuccessMessageMixin,UpdateView):
    model = Post
    template_name = "registration/post-create-update.html"
    success_url = reverse_lazy('account:update_post')
    success_message = "پست شما با موفقیت تغییر یافت"
    
class PostDelete(AdminAccessMixin,DeleteView):
    model = Post
    template_name = "registration/post_confirm_delete.html"
    success_url = reverse_lazy('account:home')
    success_message = "پست شما با موفقیت حذف شد"
    