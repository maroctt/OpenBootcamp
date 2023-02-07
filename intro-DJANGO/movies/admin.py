from django.contrib import admin

# Register your models here.
from .models import Actor, Director, Genre, Language, Movie

admin.site.register(Actor)
# admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(Movie)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['last_name', 'first_name',
              ('date_of_birth', 'date_of_death')]


admin.site.register(Director, DirectorAdmin)

# Other way of doing the same as above


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'director', 'rating')

    fieldsets = (
        (None, {
            'fields': ('title', 'poster', 'director', 'release_date')
        }),
        ('Info', {
            'fields': ('genre', 'actors', 'language')
        }),
        ('Others', {
            'fields': ('duration', 'rating')
        })
    )
