from django.contrib import admin

# Register your models here.
from walks.models import Walk, Stop, Picture
admin.site.register(Walk)
admin.site.register(Stop)
admin.site.register(Picture)
