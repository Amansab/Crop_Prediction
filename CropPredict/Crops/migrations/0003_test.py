# Generated by Django 4.2.3 on 2023-10-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Crops", "0002_alter_register_firstname"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("n", models.FloatField(max_length=10)),
                ("p", models.FloatField(max_length=10)),
                ("k", models.FloatField(max_length=10)),
                ("temp", models.FloatField(max_length=10)),
                ("pH", models.FloatField(max_length=10)),
                ("humidity", models.FloatField(max_length=10)),
                ("rain", models.FloatField(max_length=10)),
            ],
        ),
    ]