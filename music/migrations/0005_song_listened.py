# Generated by Django 5.1.6 on 2025-03-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='listened',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
