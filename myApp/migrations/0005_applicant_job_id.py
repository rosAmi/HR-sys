# Generated by Django 5.0.1 on 2024-02-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0004_alter_applicant_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="applicant",
            name="job_id",
            field=models.CharField(default="0", max_length=50),
        ),
    ]
