from django.contrib import admin
# Register your models here.
from .models import Movies, Review

admin.site.register(Movies)
admin.site.register(Review)
