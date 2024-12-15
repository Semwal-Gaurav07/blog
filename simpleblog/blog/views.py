from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm

# Home view
def home_view(request):
    cat_menu = Category.objects.all()
    posts = Post.objects.all().order_by('-post_date')  # Or you can use your list view logic
    return render(request, 'home.html', {
        'cat_menu': cat_menu,
        'posts': posts,
    })

# Article detail view
def article_detail_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    cat_menu = Category.objects.all()
    total_likes = post.total_likes()

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    context = {
        'post': post,
        'cat_menu': cat_menu,
        'total_likes': total_likes,
        'liked': liked,
    }
    return render(request, 'article_details.html', context)

# Add post view
def add_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'add_post.html', {'form': form})

# Update post view
def update_post_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('article-detail', pk=post.id)
    else:
        form = EditForm(instance=post)

    return render(request, 'update_post.html', {'form': form})

# Delete post view
def delete_post_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'delete_post.html', {'post': post})

# Add comment view
def add_comment_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('article-detail', pk=post.id)
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})

# Add category view
def add_category_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'add_category.html', {'form': form})

# Category list view
def category_list_view(request):
    cat_menu = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu': cat_menu})

# Posts filtered by category
def category_view(request, cats):
    category_name = cats.replace('-', ' ').title()
    category_posts = Post.objects.filter(category__iexact=category_name)
    return render(request, 'categories.html', {
        'cats': category_name,
        'category_posts': category_posts,
    })

# Like view
def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
