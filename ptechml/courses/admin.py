from django.contrib import admin
from .models import Course, Card, UsersStats

# admin.site.register(Card)
# admin.site.register(UsersStats)
# Register your models here.
class CardInline(admin.StackedInline):
    model = Card
    fields = ['title', 'text', 'queue']
@admin.register(Course)
class СourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    inlines = [CardInline]

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'text', 'queue')
    list_filter = ('queue', )

@admin.register(UsersStats)
class UsersStatsAdmin(admin.ModelAdmin):
    list_display = ('course', 'status', 'time')


