from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import generic

from blog.forms import PostForm
from blog.models import Post


def profile(request):
    return render(request, 'blog/profile.html')

def resume(request):
    return render(request, 'blog/resume.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')

def calculator(request):
    return render(request, 'blog/calculator_site.html')

def game(request):
    return render(request, 'blog/game_site.html')

def image_viewer(request):
    return render(request, 'blog/image_viewer_site.html')


def contact(request):
    return render(request, 'blog/contact.html')

def design(request):
    return render(request, 'blog/design.html')

# def board(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/board.html', {'posts': posts} )

class postDetailView(generic.DetailView):
    model = Post





class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/board.html'

    context_object_name = 'posts'
    queryset = Post.objects.filter(published_date__lte=timezone.now())
    paginate_by = 7

class savePostListView(generic.ListView):
    model = Post
    template_name = 'blog/save_board.html'

    context_object_name = 'posts'
    queryset = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    paginate_by = 7


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=pk)


def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                # post.author = request.user
                post.author = User.objects.get(id=1)
                post.save()
                return redirect('blog:post_detail', pk=post.pk)

            else:
                form = PostForm()
                return render(request, 'blog/post_edit.html', {'form': form})

        else:
            form = PostForm()
            return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                # post.author = request.user
                post.author = User.objects.get(id=1)
                post.save()
                return redirect('blog:post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:board')
