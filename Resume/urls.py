"""
URL configuration for Resume project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from project import views

# Defines the URL patterns for the project
urlpatterns = [
    # URL pattern for the admin site
    path('admin/', admin.site.urls),
    # URL pattern for the home page, mapped to the index view function in project/views.py
    path('', views.index, name='index'),
    # URL pattern for project detail, expects an integer parameter project_id, mapped to the detail view function in
    # project/views.py
    path('project/<int:project_id>', views.detail, name='detail'),
    # URL pattern for including the blog app's URLs, mapped to the 'blog.urls' module
    path('blog/', include('blog.urls')),
]

# Appends URL patterns for serving static files in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Appends URL patterns for serving media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The code includes the URL patterns for the project. The urlpatterns list contains the following patterns:
#
# admin/: URL pattern for the Django admin site. '': Root URL pattern mapped to the index view function in views.py.
# It represents the home page of the project. project/<int:project_id>: URL pattern for project detail, expecting an
# integer parameter project_id. It is mapped to the detail view function in views.py. blog/: URL pattern for
# including the blog app's URLs. It is mapped to the blog.urls module, allowing the blog app to handle URLs starting
# with "blog/". Additionally, the code appends URL patterns for serving static files and media files in development,
# using the static() function provided by Django. These patterns are based on the settings specified in settings.py
# for STATIC_URL, STATIC_ROOT, MEDIA_URL, and MEDIA_ROOT. This ensures that static files (e.g., CSS, JavaScript) and
# media files (e.g., uploaded images) are served correctly during development.
