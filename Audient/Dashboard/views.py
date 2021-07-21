from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post

# Create your views here.
def posts(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:20]
    output = ', '.join([q.post_text for q in latest_post_list])
    template = loader.get_template('dashboard/dashboard.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))