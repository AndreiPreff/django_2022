# Generated by Django 4.1 on 2022-09-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_alter_movie_budget_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Квентин Тарантино', max_length=100),
        ),
    ]