# Generated by Django 4.2.1 on 2024-05-19 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("SPA", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="habit",
            options={"verbose_name": "привычка", "verbose_name_plural": "привычки"},
        ),
    ]
