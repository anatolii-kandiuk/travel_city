from django.db import models
from django.core.exceptions import ValidationError
from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Train')
    from_city = models.ForeignKey(City,
                                  on_delete=models.CASCADE,
                                  verbose_name='From',
                                  related_name='from_city')
    to_city = models.ForeignKey(City,
                                on_delete=models.CASCADE,
                                verbose_name='To',
                                related_name='to_city')
    travel_time = models.IntegerField(verbose_name='Time')

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        ordering = ['name']

    def __str__(self):
        return 'Train #{} from {} to {}'.format(self.name, self.from_city, self.to_city)

    def clean(self, *args, **kwargs):
        if self.from_city == self.to_city:
            raise ValidationError('Data no correct')

        qs = Train.objects\
            .filter(from_city=self.from_city,
                    to_city=self.to_city,
                    travel_time=self.travel_time)\
            .exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError('Train already exist')

        return super(Train, self).clean(*args, **kwargs)