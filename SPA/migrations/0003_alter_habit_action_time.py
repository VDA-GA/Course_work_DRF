# Generated by Django 4.2.1 on 2024-05-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SPA", "0002_alter_habit_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="action_time",
            field=models.IntegerField(
                help_text="Укажите время на выполнение привычки в секундах", verbose_name="Время на выполнение"
            ),
        ),
    ]