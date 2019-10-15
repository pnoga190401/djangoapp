from django.contrib import admin

from pizza import models

admin.site.register(models.Pizza)
admin.site.register(models.Skladnik)
