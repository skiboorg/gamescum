from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import PlayerProfile

class ProfileInline(admin.StackedInline):
    model = PlayerProfile
    can_delete = False
    # verbose_name_plural = 'Профиль '
    fk_name = 'user'
    extra = 0
    max_num = 0

class PlayerProfileAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(PlayerProfileAdmin, self).get_inline_instances(request, obj)

class PlayerProfileAdmin1(admin.ModelAdmin):
    # list_display = ['name','discount']
    list_display = [field.name for field in PlayerProfile._meta.fields]

    exclude = ['user'] #не отображать на сранице редактирования
    class Meta:
        model = PlayerProfile



admin.site.unregister(User)
admin.site.register(User, PlayerProfileAdmin)
admin.site.register(PlayerProfile, PlayerProfileAdmin1)



