# Generated by Django 2.1.3 on 2018-11-29 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0001_initial'),
        ('users', '0002_auto_20181129_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerprofile',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='playerprofile',
            name='squad_id',
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='squad',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='squads.Squad'),
            preserve_default=False,
        ),
    ]