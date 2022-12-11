from django.contrib import admin

# Register your models here.

from .models import Experience, Education


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['created']


admin.site.register(Experience, ProjectAdmin)
admin.site.register(Education, ProjectAdmin)
