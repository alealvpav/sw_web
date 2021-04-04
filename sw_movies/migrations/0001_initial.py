# Generated by Django 2.2.19 on 2021-04-04 21:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import sw_movies.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200, verbose_name='Title')),
                ('episode_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Episode')),
                ('director', models.CharField(default='', max_length=200, verbose_name='Director')),
                ('image', models.ImageField(blank=True, null=True, upload_to=sw_movies.utils.get_file_path, verbose_name='Image')),
                ('characters', models.ManyToManyField(blank=True, to='sw_movies.Character', verbose_name='Characters')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=sw_movies.utils.get_file_path, verbose_name='Image')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_movies.Character')),
            ],
        ),
    ]