# Generated by Django 4.1 on 2022-09-27 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_rename_actor_acto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Acto',
            new_name='Actor',
        ),
    ]