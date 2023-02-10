from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'currency', 'rating_status']
    list_editable = ['rating', 'year', 'currency']
    ordering = ['rating']
    list_per_page = 4

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov):
        if mov.rating < 50:
            return 'Зачем это смотреть?'
        elif mov.rating < 70:
            return 'Разок можно глянуть'
        elif mov.rating < 85:
            return 'Отлично'
        return 'ТОП!'
