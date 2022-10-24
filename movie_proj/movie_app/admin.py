from django.contrib import admin
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

# Register your models here.

admin.site.register(Actor)
admin.site.register(Director)
# admin.site.register(DressingRoom)

@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):

    list_display = ['floor', 'number', 'actor']


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'низкий'),
            ('от 40 до 60', 'средний'),
            ('от 60 до 80', 'высокий'),
            ('от 80 до 100', 'наивысший')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        elif self.value() == 'от 40 до 60':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        elif self.value() == 'от 60 до 80':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        elif self.value() == 'от 80 до 100':
            return queryset.filter(rating__gte=80)
        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # exclude = ['slug']
    # readonly_fields = ['budget']
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'rating', 'year', 'director', 'budget', 'currency', 'rating_status']
    list_editable = ['rating', 'year', 'director', 'budget', 'currency']
    filter_horizontal = ['actors']
    ordering = ['-rating', 'name']
    list_per_page = 15
    actions = ['set_dollars', 'set_euros', 'set_roubles']
    search_fields = ['name', 'rating']
    list_filter = ['name', 'year', RatingFilter]

    @admin.display(ordering='rating', description='Оценка')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return f'Зачем это смотреть?!'
        if mov.rating < 70:
            return f'Разок можно глянуть'
        if mov.rating <= 80:
            return f'Зачет!'
        return f'Топчик!'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.USD)
        self.message_user(request, f'Было обновлено записей - {count_updated}')

    @admin.action(description='Установить валюту в евро')
    def set_euros(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(request, f'Было обновлено записей - {count_updated}')

    @admin.action(description='Установить валюту в рубли')
    def set_roubles(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.RUB)
        self.message_user(request, f'Было обновлено записей - {count_updated}')
