# Generated by Django 5.0.1 on 2024-02-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("created", models.DateField(auto_now_add=True)),
                ("url", models.URLField()),
                ("email", models.EmailField(max_length=254)),
                ("details", models.TextField()),
            ],
            options={
                "ordering": ["created"],
            },
        ),
    ]
