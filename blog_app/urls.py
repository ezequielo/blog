from django.conf.urls import patterns, url
from blog_app import views

urlpatterns = patterns('',

#     url(r'^$', views.IdexView.as_view(), name='index'),
#     url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
#     url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.all_posts, name='post'), 
    url(r'^post/(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^category/(?P<cat_id>\d+)/$', views.category, name='category'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^password_restore/$', views.password_restore, name='password_restore'),
    url(r'^create_account/$', views.create_account, name='create_account'),
    
    
    
    
)