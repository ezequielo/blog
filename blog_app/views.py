from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from blog_app.models import Post, Comment 
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone



def index(request):
    latest_post_list = Post.objects.order_by('pub_date')[:5]
    return render(request, 'blog_app/index.html', {'latest_post_list':latest_post_list})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request,'blog_app/detail.html',{'post':post})
 
 
# def detail(request, poll_id):
# #     try:
# #         poll = Poll.objects.get(pk=poll_id)
# #     except Poll.DoesNotExist:
# #         raise Http404
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/detail.html', {'poll':poll})
#  
#  
# def results(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/results.html', {'poll': poll})
# 
# 
# def vote(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the poll voting form.
#         return render(request, 'polls/detail.html', {
#             'poll': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))