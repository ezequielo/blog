from django.shortcuts import render, get_object_or_404
from blog_app.models import Post, Comment 
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import request
from django.utils import timezone
# from django.views import generic


def index(request):
    latest_post_list = Post.objects.order_by('pub_date')[:5]
    return render(request, 'blog_app/index.html', {'latest_post_list':latest_post_list})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    # if write a comment
    if request.method=='POST':
        if request.POST.get("text"):
            text = request.POST.get("text")
            c = Comment.objects.create(fk_post = post, text = text, pub_date = timezone.now())
            c.save()
    
    # load all comments
    comments = Comment.objects.filter(
            fk_post=post_id
        ).order_by('pub_date')
    
    return render(request,'blog_app/detail.html',{'post':post, 'comment_list':comments})

        
def nav(request):
    return render(request,'blog_app/navbar.html',{'nothing':'nothing'})


def sidebar(request):
    return render(request,'blog_app/sidebar.html',{})
    
    