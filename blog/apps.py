from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
# The code defines a BlogConfig class that extends the AppConfig class from Django. It is used to configure the
# application named 'blog'.
#
# The default_auto_field attribute specifies the default auto field to use for model primary keys. In this case,
# it is set to 'django.db.models.BigAutoField', indicating the use of a big integer field for auto-generated primary
# keys. The name attribute specifies the name of the application, which is 'blog' in this case. It is used to
# uniquely identify the application and is typically used in various Django configurations.
