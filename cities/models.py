from django.db import models


class City(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='City')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['name']
