from django.contrib import admin
from . import models


admin.site.register(models.Author)
admin.site.register(models.Genre)
admin.site.register(models.Condition)
admin.site.register(models.Book)