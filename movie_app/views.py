from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Max, Min, Count, Avg
from .models import Movie


def show_all_movie(request):
    movies = Movie.objects.order_by('name')
    agg = movies.aggregate(Avg('budget'), Min('rating'), Max('rating'), Count('id'))
    agg['budget__avg'] = round(agg['budget__avg'])
    return render(request, 'movie_app/all_movies.html', context={'movies': movies,
                                                                 'agg': agg})


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', context={'movie': movie})
