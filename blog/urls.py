from django.urls import path
from . import views


# path is used to define url patterns
#we are importing app's views. these are python functions that handle what to display when someone visits the url
urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]

 #  1st url -> This says: when someone visits the root of your site ( 127.0.0.1:8000/),  call the function post_list inside views.py to generate the page.
###url-2
#post/ means that the URL should begin with the word post followed by a /
#<int:pk> means django expects an integer value and will transfer it to a view as a variable called pk
#then we need a / again before finishing the URL.