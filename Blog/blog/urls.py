"""Defines URL patterns for blog"""

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    #Home page
    path('', views.index, name = 'index'),
    path('all_blogs/', views.blogs, name = 'blogs'),
    #So when we go to the all_blogs page we calls the blogs function in the view.py file and pass the argument 'blog' to it as the request

    #Detail page for a single topic
    path('all_blogs/<int:blog_id>/', views.blog, name = 'blog'),
    #So this was failig at first because I was calling the blog function in views.blog... and I was returning the blog and blog_posts key-value
    #That dictionary was then getting passed to the blog.html file
    #Which tries to loop through blog_posts. Where I failed at first was I had erroneously named blog_posts as blog_post. Missing the s
    #The for loop therefore could not find a blog_posts key. And assumed there was no data to be found

    #Page for adding a new topic
    path('new_blog/', views.new_blog, name = 'new_blog'),
    
    #Page for adding a new entry
    path('new_blog_post/<int:blog_id>/', views.new_blog_post, name = 'new_blog_post'),

    #Page for editing an entry
    path('edit_blog_post/<int:blog_post_id>/', views.edit_blog_post, name = 'edit_blog_post'),
]