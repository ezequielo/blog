# Shortcuts
from django.shortcuts import render, render_to_response, get_object_or_404
# Models
from blog_app.models import Post, Comment, Category

from django.http.response import HttpResponseRedirect

from django.core.urlresolvers import reverse
from django.core.context_processors import request
from django.core.context_processors import csrf
# Auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login

from django.utils import timezone
# Forms
from blog_app.forms import CreateAccountForm, ContactForm
# Loggin
import logging
logger = logging.getLogger(__name__)


def myfunction():
    logger.debug("this is a debug message!")
 
def myotherfunction():
    logger.error("this is an error message!!")

# from django.views import generic


def index(request):
    logging.info('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    vals = {}
    vals['latest_post_list'] = Post.objects.order_by('pub_date')[:5]
    vals['categories_list'] = Category.objects.order_by('name')
    return render(request, 'blog_app/index.html', vals)


def all_posts(request):
    vals = {}
    vals['latest_post_list'] = Post.objects.order_by('pub_date')
    vals['categories_list'] = Category.objects.order_by('name')
    return render(request, 'blog_app/index.html', vals)
    
    
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # if write a comment
    if request.method=='POST':
        if request.POST.get("text"):
            text = request.POST.get("text")
            user = request.user
            c = Comment.objects.create(fk_post = post, text = text, pub_date = timezone.now(), fk_user = user)
            c.save()
            return HttpResponseRedirect('.')
    # load all comments
    comments = Comment.objects.filter(
            fk_post=post_id
        ).order_by('pub_date')
    
    return render(request,'blog_app/detail.html',{'post':post, 'comment_list':comments})


def login(request):
    url = 'blog_app/login.html'
    vals = {}
    vals.update(csrf(request))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/blog')
            else:
                vals['error_msg'] ='Usuario inactivo!'
        else:
            vals['error_msg'] = 'Usuario o contrasenya incorrecta!'
    return render(request, url, vals)
    
    
def logout_view(request):
    logout(request)
    return index(request)
    

def about(request):
    # TODO
    return render(request,'blog_app/about.html',{})
    
def password_restore(request):
    # TODO
    return render(request, 'blog_app/password_restore.html', {})


def create_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/blog')
    else:
        form = CreateAccountForm()
    return render(request, 'blog_app/create_account.html', {'form':form})


def category(request, cat_id):
    vals = {}
    vals['categories_list'] = Category.objects.order_by('name')
    vals['latest_post_list'] = Post.objects.filter(
        fk_cat=cat_id
    ).order_by('pub_date')
    return render(request, 'blog_app/index.html', vals)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/blog')
    else:
        form = ContactForm()
    return render(request, 'blog_app/contact.html', {'form':form})
