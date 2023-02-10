from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year']
    list_editable = ['rating', 'year']
    ordering = ['rating']
    list_per_page = 4
