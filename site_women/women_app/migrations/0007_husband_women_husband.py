# Generated by Django 5.0.7 on 2024-07-24 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0006_tagpost_alter_women_cat_women_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Husband',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='women',
            name='husband',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wuman', to='women_app.husband'),
        ),
    ]
