from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, HashTag, Comment
from django.contrib.auth.views import login_required
from accounts.models import User

# Create your views here.
def index(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    form = CommentForm
    context = {
        'posts': posts,
        'comments': comments,
        'form': form,
    }
    return render(request, 'posts/index.html', context)


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for word in post.content.split():
                if word.startswith('#'):
                    # hashtag 추가
                    hashtag = HashTag.objects.get_or_create(content=word)[0] # (obj, True or False)
                    post.hashtags.add(hashtag)
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)


def hashtags(request, id):
    hashtag = get_object_or_404(HashTag, id=id)
    
    posts = hashtag.taged_post.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def like(request, id):
    post = get_object_or_404(Post, id=id)
    user = request.user

    if user in post.likes_users.all():
        post.likes_users.remove(user)
    else:
        post.likes_users.add(user)
    
    return redirect('posts:index')



def follow(request, id):
    you = get_object_or_404(User, id=id)
    me = request.user
    
    if you != me:
        if you.followers.filter(id=me.id):
        # if me in you.followers.all():
            you.followers.remove(me)
        else:
            you.followers.add(me)

    return redirect("posts:index")


    
def create_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
    return redirect("posts:index")


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect("posts:index")