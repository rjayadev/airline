# Generated by Django 3.0.6 on 2020-05-12 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='orgin',
            new_name='origin',
        ),
    ]
