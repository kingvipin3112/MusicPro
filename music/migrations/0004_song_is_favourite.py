# Generated by Django 2.0.7 on 2018-08-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_remove_song_is_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
