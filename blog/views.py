from django.shortcuts import render

"""
   Views receive the request as well as parameters passed from url.
   They fetch the info from the model,probably addong some logic
   Create response by filling template with fetched info
   they are python functions that take request as parameter and return Httpresponse
"""

def post_list(request):
    return render(request,'blog/post_list.html',{})
    # when this function is called it internally calls render which returns the final output
