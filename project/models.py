from django.db import models
from django.urls import reverse


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)  # Field to store the project title
    description = models.CharField(max_length=250)  # Field to store the project description
    image = models.ImageField(upload_to='resume/images/')  # Field to store the project image (uploaded to
    # 'resume/images/' directory)
    url = models.URLField(blank=True)  # Field to store the project URL (optional)

    def __str__(self):
        return self.title  # Returns the title as the string representation of the project object

    def get_absolute_url(self):
        return reverse('detail', kwargs={
            'project_id': self.id
        })
#
# The code defines a Django model called Project that represents a project. Here's a breakdown of the model:
#
# title: CharField to store the project title with a maximum length of 50 characters.
# description: CharField to store the project description with a maximum length of 250 characters.
# image: ImageField to store the project image. The images are uploaded to the 'resume/images/' directory.
# url: URLField to store the project URL. This field is optional and can be left blank.
# The model also includes two methods:
#
# __str__(): This method returns the string representation of the project object, which is its title.
# get_absolute_url(): This method returns the URL for the project's detail view. It uses the reverse() function to
# dynamically generate the URL by passing the view name 'detail' and the project's ID as keyword arguments.
