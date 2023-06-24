from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()  # Retrieve all projects from the database
    context = {
        'projects': projects  # Pass the projects to the template context
    }
    return render(request, 'project/index.html', context)  # Render the index.html template with the context

def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)  # Retrieve a specific project by its ID from the database
    context = {
        'project': project  # Pass the project to the template context
    }
    return render(request, 'project/detail.html', context)  # Render the detail.html template with the context
#
# The code defines two views for a Django project. Here's a breakdown of each view:
#
# index: This view retrieves all projects from the Project model and passes them as a context variable named
# 'projects'. It renders the 'project/index.html' template with the context.
#
# detail: This view retrieves a specific project based on its project_id from the Project model using the
# get_object_or_404 function. It passes the project as a context variable named 'project'. It renders the
# 'project/detail.html' template with the context.
#
# The views are responsible for fetching the necessary data from the model and passing it to the respective templates
# for rendering.