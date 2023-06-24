from django.db import models
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Returns the absolute URL for the blog's detail view
        return reverse('blog:blog_detail', kwargs={
            'blog_id': self.id
        })
# The code defines a Blog model with fields for title, description, and date. The __str__ method is overridden to
# provide a human-readable representation of the blog object (the title). The get_absolute_url method returns the
# absolute URL for the blog's detail view, using the reverse function to generate the URL based on the blog_id
# parameter. This allows for easy linking to the detail view of a specific blog.
