# Generated by Django 4.2.2 on 2024-05-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lobby', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
    ]