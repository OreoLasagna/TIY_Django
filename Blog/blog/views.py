from django.shortcuts import render, redirect

from .models import Blog, Blog_Post
from .forms import Blog_Form, Blog_Post_Form

# Create your views here.
def index(request):
    """The home page for Blog."""
    return render(request, 'blog/index.html')
    #Looking at the blog folder and the index.html file in it

def blogs(request):
    """Show all blogs"""
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context)

def blog(request, blog_id):
    """Show a single blog and all of its entries"""
    blog = Blog.objects.get(id = blog_id)
    blog_posts = blog.blog_post_set.order_by('-date_added')
    #THE LOWERCASE ENTRY IS REFERENCING THE BLOG POST CLASS IN THE MODELS.PY FILE.
    #IF YOU WANT TO USE FOREIGN_KEYS PROPERLY AND GRAB MANY ITEMS ASSOCIATED TO A SINGLE PIZZA OR TOPIC FOR EXAMPLE
    #YOU WOULD GO (name goes here).(LOWERCASE CLASS NAME)_set.
    context = {'blog': blog, 'blog_posts': blog_posts}
    return render(request, 'blog/blog.html', context)

def new_blog(request):
    """Add a new blog"""
    #Make this match the functions in the urls.py folder within the blog folder
    if request.method != 'POST':
        #No data submitted; create a blank form
        #When the User first hits or enters this page their browser is sending a GET request
        #So this is triggered when first hitting the page. If the user submits a form then that is a POST request
        form = Blog_Form()

    else:
        #POST data submitted; process data
        form = Blog_Form(data = request.POST)
        if form.is_valid():
            form.save()
            #The save method writes this to the DB
            return redirect('blog:blogs')
            #I think this redirect is saying use the the topics function above which calls a new HTML page to redirect you to.


    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blog/new_blog.html', context)

def new_blog_post(request, blog_id):
    """Add a new entry for a particular topic"""
    blog = Blog.objects.get(id=blog_id)
    #Grabbing an individual blog

    if request.method != 'POST':
        #No data submitted; create a blank form
        form = Blog_Post_Form()

    else:
        #POST data submitted; process data.
        form = Blog_Post_Form(data = request.POST)
        if form.is_valid():
            new_blog_post = form.save(commit = False)
            new_blog_post.blog = blog
            new_blog_post.save()
            return redirect('blog:blog', blog_id = blog_id)
            #Telling it to call the topic function above

    #Display a blank or invalid form
    context = {'blog': blog, 'form': form}
    return render(request, 'blog/new_blog_post.html', context)

def edit_blog_post(request, blog_post_id):
    """Edit an existing entry"""
    blog_post = Blog_Post.objects.get(id = blog_post_id)
    blog = blog_post.blog

    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry.
        form = Blog_Post_Form(instance = blog_post)
    else:
        #POST data submitted; process data
        form = Blog_Post_Form(instance = blog_post, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:blog', blog_id = blog.id)
            #Telling it to call the blog function above

    context = {'blog_post': blog_post, 'blog': blog, 'form': form}
    return render(request, 'blog/edit_blog_post.html', context) 
