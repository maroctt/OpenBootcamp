from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Actor(models.Model):
    """Model representing a movie actor"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Director(models.Model):
    """Model representing a movie director"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this director."""
        return reverse('director-detail', args=[str(self.id)])


class Genre(models.Model):
    """Model representing a movie genre"""
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Language(models.Model):
    """Model representing a movie language"""
    language = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.language


class Movie(models.Model):
    """Model representing a movie"""
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey(
        'Director', on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)
    language = models.ManyToManyField(Language)
    duration = models.FloatField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True, validators=[
                               MaxValueValidator(10.0), MinValueValidator(0.0)])
    poster = models.ImageField(upload_to='movie_poster', default='default.jpg')

    class Meta:
        ordering = ['title', 'release_date']

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this movie."""
        return reverse('movie-detail', args=[str(self.id)])
