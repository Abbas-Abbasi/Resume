from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # URL pattern for displaying all blogs
    path('', views.all_blogs, name="all_blogs"),

    # URL pattern for displaying details of a specific blog
    path('<int:blog_id>', views.blog_detail, name="blog_detail")
]
# The code defines the URL patterns for the blog app. The first URL pattern ('') maps to the all_blogs view function,
# which displays all blogs. The second URL pattern ('<int:blog_id>') maps to the blog_detail view function,
# which displays the details of a specific blog based on the blog_id parameter. The name attribute is used to provide
# a unique name to each URL pattern, allowing them to be easily referenced in templates and views.
