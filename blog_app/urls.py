from django.conf.urls import patterns, url
from blog_app import views

urlpatterns = patterns('',

#     url(r'^$', views.IdexView.as_view(), name='index'),
#     url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
#     url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
)