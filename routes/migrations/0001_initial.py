# Generated by Django 4.0.1 on 2022-01-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Route')),
                ('from_city', models.CharField(max_length=150, verbose_name='From')),
                ('to_city', models.CharField(max_length=150, verbose_name='To')),
                ('travel_time', models.IntegerField(verbose_name='Time')),
                ('across_cities', models.ManyToManyField(to='trains.Train', verbose_name='Across cities')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
                'ordering': ['name'],
            },
        ),
    ]
