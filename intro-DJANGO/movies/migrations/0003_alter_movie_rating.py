# Generated by Django 4.1.6 on 2023-02-05 11:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_alter_director_options_alter_movie_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(10.0),
                    django.core.validators.MinValueValidator(0.0),
                ],
            ),
        ),
    ]
