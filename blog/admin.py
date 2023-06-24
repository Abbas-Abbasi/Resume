from django.contrib import admin
from .models import Blog

# Register your models here.

admin.site.register(Blog)

# The code registers the Blog model in the Django admin interface.
#
# The from django.contrib import admin line imports the admin module from the django.contrib package, which provides
# the functionality for managing models in the admin interface. The from .models import Blog line imports the Blog
# model from the current package. The admin.site.register(Blog) line registers the Blog model with the admin site,
# allowing it to be managed through the admin interface. Once registered, you can perform CRUD (Create, Read, Update,
# Delete) operations on Blog objects using the admin site.
