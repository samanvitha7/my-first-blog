from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

"""
   Views receive the request as well as parameters passed from url.
   They fetch the info from the model,probably addong some logic
   Create response by filling template with fetched info
   they are python functions that take request as parameter and return Httpresponse
"""

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})
    # when this function is called it internally calls render which returns the final output

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
