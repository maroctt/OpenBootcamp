# Generated by Django 4.1.6 on 2023-02-06 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_remove_movie_language_movie_language"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="movie", options={"ordering": ["title", "release_date"]},
        ),
        migrations.RenameField(
            model_name="movie", old_name="release_year", new_name="release_date",
        ),
    ]