from import_export import resources
from .models import *
from django.contrib.auth import user

class user_resource (resources.ModelResource):
    class Meta:
        model = user
        exclude=('id',)

class User_resource (resources.ModelResource):
    class auth_user_resource (resources.ModelResource):
        class Meta:
            model = user
            exclude=('id',)


