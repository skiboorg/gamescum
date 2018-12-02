from django.db import models
from django.contrib.auth.models import User
from squads.models import Squad
from events.models import Event


class PlayerProfile(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    squad       = models.ForeignKey(Squad, blank=True, null=True, on_delete=models.CASCADE)
    event       = models.ForeignKey(Event, blank=True, null=True, on_delete=models.CASCADE)
    discord_id  = models.CharField(max_length=10, blank=False, unique=True)
    steam_id    = models.CharField(max_length=10, blank=False, unique=True)
    wallet      = models.IntegerField(default=0, blank=True)
    rating      = models.DecimalField(max_digits=4, decimal_places=3, default=1)
    squad_leader = models.BooleanField(default=False)
    vip         = models.BooleanField(default=False)
    kills       = models.IntegerField(default=0, blank=True)
    deaths      = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return 'Профиль игрока %s' % self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
