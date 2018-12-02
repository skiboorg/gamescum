from django.db import models

class News(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    full_text = models.TextField(blank=False)
    show_on_homepage = models.BooleanField(blank=False,default=False)
