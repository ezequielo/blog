from django.shortcuts import render, get_object_or_404
from blog_app.models import Post, Comment 
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.views import generic


def index(request):
    latest_post_list = Post.objects.order_by('pub_date')[:5]
    return render(request, 'blog_app/index.html', {'latest_post_list':latest_post_list})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(
            fk_post=post_id
        ).order_by('pub_date')
    
    return render(request,'blog_app/detail.html',{'post':post, 'comment_list':comments})