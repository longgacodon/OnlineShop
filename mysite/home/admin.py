from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'gender','email', 'phone', 'birthday', 'address', 'day_joined', 'updated']
	list_filter = ['name', 'gender', 'birthday', 'day_joined', 'updated']
	list_editable = ['name', 'gender', 'address']