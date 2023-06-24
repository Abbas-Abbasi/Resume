from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Sets the default auto field for the app to BigAutoField
    name = 'project'  # Specifies the name of the app as 'project'

#
# The code defines a Django app configuration class called ProjectConfig for the 'project' app. Here's a breakdown of
# the configuration:
#
# default_auto_field: Specifies the default auto field to be used for the models in the app. In this case,
# it is set to 'django.db.models.BigAutoField', indicating that a BigAutoField will be used as the default primary
# key field for the models. This is typically used for models with large record counts. name: Specifies the name of
# the app as 'project'. This is the name used to identify the app in Django and should match the name of the app
# directory.
