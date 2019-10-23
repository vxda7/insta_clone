from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CostomUserCreationForm
from .models import User
from posts.models import Post
from posts.forms import CommentForm
# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CostomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CostomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect("accounts:login")


def user_page(request, id):
    user_info = get_object_or_404(User, id=id)
    posts = Post.objects.filter(user=user_info)
    form = CommentForm
    context = {
        'user_info':user_info,
        'posts': posts,
        'form': form,
    }
    return render(request, 'accounts/user_page.html', context)


def follow(request, id):
    you = get_object_or_404(User, id=id)
    me = request.user
    
    if you != me:
        if you.followers.filter(id=me.id):
        # if me in you.followers.all():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect("accounts:user_page", id)
    
    
