from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/posts/list.html',
                  {'posts': posts})


def post_deatil(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             status = Post.Status.PUBLISHED)
    return render(request,
                  'blog/posts/detail.html',
                  {"post": post})