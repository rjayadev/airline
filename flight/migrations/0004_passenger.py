# Generated by Django 3.0.6 on 2020-05-12 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_auto_20200512_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('fights', models.ManyToManyField(blank=True, related_name='passenger_list', to='flight.Flight')),
            ],
        ),
    ]
