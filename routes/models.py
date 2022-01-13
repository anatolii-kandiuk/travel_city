from django.db import models
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name='Route',
                            unique=True)
    from_city = models.CharField(max_length=150, verbose_name='From')
    to_city = models.CharField(max_length=150, verbose_name='To')
    across_cities = models.ManyToManyField(Train, verbose_name='Across cities')
    travel_time = models.IntegerField(verbose_name='Time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['name']