# Generated by Django 4.1.2 on 2022-10-05 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]