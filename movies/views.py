from django.shortcuts import render, get_object_or_404, redirect
from .models import Movies, MovieRating
from django.db.models import Avg

def index(request):
    movies = Movies.objects.all()
    
    # Filters
    select_genre = request.GET.get('genre', 'all')
    select_year = request.GET.get('year', 'all')
    
    if select_genre != 'all':
        movies = movies.filter(genre__iexact=select_genre)  # case-insensitive exact match
    
    if select_year != 'all':
        movies = movies.filter(year=select_year)
    
    # Search filter
    search_query = request.GET.get('q', '')
    if search_query:
        movies = movies.filter(title__icontains=search_query)
    
    # Annotate average rating
    movies = movies.annotate(avg_rating=Avg('ratings__rating'))
    
    # Dropdown options
    genres = Movies.objects.values_list('genre', flat=True).distinct()
    years = Movies.objects.values_list('year', flat=True).distinct().order_by('year')
    
    return render(request, 'movies/index.html', {
        'movies': movies,
        'genres': genres,
        'years': years,
        'select_genre': select_genre,
        'select_year': select_year,
        'search_query': search_query,
    })

    
    # return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id)

    if request.method == "POST":
        rating_value = int(request.POST.get('rating'))
        # Save rating anonymously
        MovieRating.objects.create(movie=movie, rating=rating_value)
        return redirect('movies:detail', movie_id=movie_id)

    # Calculate average rating
    avg_rating = MovieRating.objects.filter(movie=movie).aggregate(Avg('rating'))['rating__avg']

    return render(request, 'movies/detail.html', {
        'movie': movie,
        'avg_rating': avg_rating,
    })

def home(request):
    return render(request, 'home.html')
