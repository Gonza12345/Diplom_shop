from django.contrib import admin
from .models import Category, Product

class Emp_project_Admin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
# Register your models here.
class Priority_Admin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
# Register your models here.
admin.site.register(Emp_project, Emp_project_Admin)
admin.site.register(Priority, PriorityAdmin)