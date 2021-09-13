
from blog.models import Post
from django import http
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404

class SuperUserAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("/")
			
class AdminAccessMixin():
	def dispatch(self, request, pk,*args, **kwargs):
		post = get_object_or_404(Post,pk=pk)
		if request.user.is_superuser or post.author == request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("/")

class PostFieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			self.fields = ["author","title","slug","category","description","thumbnail","publish","status"]
		elif request.user.is_staff:
			self.fields = ["title","slug","category","description","thumbnail","publish","status"]
		else:
			raise Http404
		return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
	def form_valid(self,form):
		if self.request.user.is_superuser:
			form.save()
		else:
			self.obj = form.save(commit=False)
			self.obj.author = self.request.user
		return super().form_valid(form)
