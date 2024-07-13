from django.contrib import admin
from .models import contactModel
# Register your models here.

@admin.register(contactModel)
class contactModelRegister(admin.ModelAdmin):
      list_display=['id', 'name', 'email', 'subject', 'message']
