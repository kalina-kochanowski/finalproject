# Generated by Django 4.2.7 on 2025-03-02 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
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
                ("name", models.CharField(max_length=200, verbose_name="Username")),
                ("bio", models.TextField(verbose_name="Biography")),
                ("slug", models.SlugField(blank=True, max_length=200, unique=True)),
            ],
        ),
    ]
