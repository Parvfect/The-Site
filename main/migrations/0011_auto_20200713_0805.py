# Generated by Django 3.0.8 on 2020-07-13 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_readinglist_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readinglist',
            name='status',
        ),
        migrations.AddField(
            model_name='readinglist',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
