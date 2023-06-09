# Generated by Django 4.2 on 2023-04-13 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=186, unique=True)),
                ('slug', models.SlugField(max_length=186)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=186)),
                ('slug', models.SlugField(max_length=186)),
                ('menu', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu.menu')),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='menu.menu')),
            ],
        ),
    ]
