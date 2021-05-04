from django.contrib import admin
from .models import piece,MO, project
from import_export.admin import ImportExportModelAdmin
from create.models import user
from django.contrib.auth.models import User
from django.db import models
# Register your models here.
admin.site.register(piece)
admin.site.register(MO)
admin.site.register(project)
@admin.register(user)
class UserAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name", "e_mail", "is_online")
    pass

