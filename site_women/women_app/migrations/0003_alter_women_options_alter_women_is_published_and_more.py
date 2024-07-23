# Generated by Django 5.0.7 on 2024-07-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0002_women_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0),
        ),
        migrations.AlterField(
            model_name='women',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
