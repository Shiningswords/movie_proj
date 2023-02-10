from django.contrib import admin
from .models import Movie
from django.db.models import QuerySet


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'currency', 'rating_status']
    list_editable = ['rating', 'year', 'currency']
    ordering = ['rating']
    list_per_page = 4
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name']
    list_filter = ['currency']

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov):
        if mov.rating < 50:
            return 'Зачем это смотреть?'
        elif mov.rating < 70:
            return 'Разок можно глянуть'
        elif mov.rating < 85:
            return 'Отлично'
        return 'ТОП!'

    @admin.action(description='Установить валюту в Доллары')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency='D')

    @admin.action(description='Установить валюту в Евро')
    def set_euro(self, request, qs: QuerySet):
        msg = qs.update(currency='E')
        self.message_user(request, f'Было обновлено {msg} записей')

