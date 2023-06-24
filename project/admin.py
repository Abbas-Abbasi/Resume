from django.contrib import admin
from .models import Project

# Register your models here.

# Registers the Project model with the admin site.
admin.site.register(Project)

# The code registers the Project model in the Django administration site. Here's a breakdown of the code:
#
# from django.contrib import admin: Imports the admin module from Django, which provides the functionality for
# managing models in the admin interface. from .models import Project: Imports the Project model from the current
# directory (app). admin.site.register(Project): Registers the Project model with the admin site. This makes the
# Project model accessible and manageable through the Django admin interface, allowing you to perform CRUD (Create,
# Read, Update, Delete) operations on Project objects.
