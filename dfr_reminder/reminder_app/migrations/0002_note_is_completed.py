# Generated by Django 4.2.18 on 2025-02-09 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
