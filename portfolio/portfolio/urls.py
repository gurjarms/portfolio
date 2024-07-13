
from django.contrib import admin
from app.views import index,contact

from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
   
    path("", index,name='index'),
    path("contact", contact, name='contact'),
]
