# Generated by Django 4.2.1 on 2024-05-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SPA", "0003_alter_habit_action_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.TimeField(help_text="В какое время выполнять привычку?", verbose_name="Время выполнения"),
        ),
    ]
