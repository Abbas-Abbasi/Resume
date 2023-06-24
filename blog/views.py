from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

# View function to display all blogs
def all_blogs(request):
    # Retrieves all Blog objects and orders them by date in descending order
    blogs = Blog.objects.order_by('-date')

    context = {
        'blogs': blogs
    }
    # Renders the 'all_blogs.html' template with the blogs data in the context
    return render(request, 'blog/all_blogs.html', context)


# View function to display details of a specific blog
def blog_detail(request, blog_id):
    # Retrieves a specific Blog object based on the provided blog_id, or returns a 404 error if not found
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog': blog
    }
    # Renders the 'blog_detail.html' template with the blog data in the context
    return render(request, 'blog/blog_detail.html', context)

# The code includes two view functions: all_blogs and blog_detail.
# The all_blogs function retrieves all Blog objects and orders them by date in descending order.
# It then renders the all_blogs.html template, passing the blogs data in the context.
# The blog_detail function retrieves a specific Blog object based on the provided blog_id parameter,
# or returns a 404 error if the blog is not found. It renders the blog_detail.html template, passing the blog data in the context.
