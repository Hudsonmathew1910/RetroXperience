from django.db import models
from django.utils import timezone

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    platform = models.CharField(max_length=100, blank=True) 
    
    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField(default=1)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.movie.title} - {self.rating}/10\nby {self.reviewer_name if self.reviewer_name else 'Anonymous'}"
    
class MovieRating(models.Model):
    movie = models.ForeignKey('Movies', on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(default=1) 
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return f"{self.movie.title} - {self.rating}/5"