# Generated by Django 5.0.7 on 2024-07-23 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]
