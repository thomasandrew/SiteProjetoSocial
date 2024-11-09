from django.contrib import admin
from . models import Gallery
from . models import Gallery_home

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Gallery_home)