from django.contrib import admin
from users.models import *


class PlayersInline (admin.TabularInline):
    model = PlayerProfile
    extra = 0


class EventAdmin(admin.ModelAdmin):
    # list_display = ['name','discount']
    list_display = [field.name for field in Squad._meta.fields]
    inlines = [PlayersInline]
    # exclude = ['info'] #не отображать на сранице редактирования
    class Meta:
        model = Event




admin.site.register(Event,EventAdmin)
# Register your models here.
