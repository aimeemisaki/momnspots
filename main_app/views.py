from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.dispatch import receiver
from .models import *


# Start Page View
class Start(TemplateView):
    template_name = "start.html"

# PostList View (Index for All without user logged in)
class Home(TemplateView):
    template_name = "post_list_all.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop_name = self.request.GET.get("shop_name")
        if shop_name != None:
            context["posts"] = Post.objects.all()
        # We add a header context that includes the search param
            context["header"] = f"Searching for {shop_name}"
        
        else:
            context["posts"] = Post.objects.all()
            context["header"] = "Mom n Spots"
        return context

# Signup View
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
        
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

# PostList View (Index)

class PostList(TemplateView):
    template_name = "post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop_name = self.request.GET.get("shop_name")
        if shop_name != None:
            context["posts"] = Post.objects.filter(shop_name__icontains=shop_name, user=self.request.user)
        # We add a header context that includes the search param
            context["header"] = f"Searching for {shop_name}"
        
        else:
            context["posts"] = Post.objects.filter(user=self.request.user)
            context["header"] = "Your Mom n Spots"
        return context

# Create PostCreate View 

class PostCreate(CreateView):
    model = Post
    fields = ['shop_name', 'img', 'story', 'neighborhood', 'category']
    success_url = reverse_lazy('post_list')
    template_name = 'post_create.html'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

# Update PostUpdate View

class PostUpdate(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['shop_name', 'img', 'story', 'category', 'neighborhood']
    success_url = reverse_lazy('post_list')

