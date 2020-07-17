# Generated by Django 3.0.7 on 2020-07-03 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200701_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('slug', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('date', models.DateField(verbose_name='date published')),
                ('slug', models.CharField(max_length=200)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.StoryCategory', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Stories',
            },
        ),
    ]
