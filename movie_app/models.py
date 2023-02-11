from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from  django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()


class Movie(models.Model):
    CURRENCY_CHOICES = [
        ('E', 'Euros'),
        ('D', 'Dollars'),
        ('R', 'Rubles')
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES, default='R')
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one_movie', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}'
