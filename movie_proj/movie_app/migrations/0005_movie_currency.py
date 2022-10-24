# Generated by Django 4.1 on 2022-09-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('E', 'Euros'), ('D', 'Dollars'), ('R', 'Roubles')], default='D', max_length=1),
        ),
    ]
