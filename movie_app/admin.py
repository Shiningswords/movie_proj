from django.contrib import admin
from .models import Movie, Director
from django.db.models import QuerySet


admin.site.register(Director)


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rate'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Low'),
            ('41-60', 'Middle'),
            ('61-85', 'High'),
            ('86-100', 'Top')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<40':
            return queryset.filter(rating__lt=41)
        elif self.value() == '41-60':
            return queryset.filter(rating__lt=61).filter(rating__gt=40)
        elif self.value() == '61-85':
            return queryset.filter(rating__lt=86).filter(rating__gt=60)
        elif self.value() == '86-100':
            return queryset.filter(rating__lt=101).filter(rating__gt=85)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ['name', 'rating', 'year', 'currency', 'rating_status']
    list_editable = ['rating', 'year', 'currency']
    ordering = ['rating']
    list_per_page = 4
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name']
    list_filter = ['currency', RatingFilter]

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

