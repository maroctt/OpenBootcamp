from django.shortcuts import render
from django.views import generic
from .models import Actor, Director, Genre, Language, Movie

# Create your views here.


def index(request):
    """View function for the homepage of site"""

    # Generate counts of some of the main objects
    num_movies = Movie.objects.all().count()
    num_directors = Director.objects.count()

    context = {
        'num_movies': num_movies,
        'num_directors': num_directors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class MovieListView(generic.ListView):
    model = Movie
    context_object_name = 'movies_list'
    template_name = 'movies_list.html'


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'movie_detail.html'


class DirectorListView(generic.ListView):
    model = Director
    context_object_name = 'director_list'
    template_name = 'director_list.html'


class DirectorDetailView(generic.DetailView):
    model = Director
    template_name = 'director_detail.html'
