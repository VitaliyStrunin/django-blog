from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    try:
        post_list = Post.published.all()
        paginator = Paginator(post_list, 3)
        page_number = request.GET.get('page', 1)
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'blog/post/list.html',
                {'posts': posts})



def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                                status=Post.Status.PUBLISHED,
                                slug=post,
                                publish__year=year,
                                publish__month=month, 
                                publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


