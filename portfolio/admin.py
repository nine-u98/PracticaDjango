from django.contrib import admin

# Register your models here.
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['created']


admin.site.register(Project, ProjectAdmin)
