# Generated by Django 4.2.1 on 2024-05-21 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="chat_id",
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="chat_id_tg"),
        ),
    ]
