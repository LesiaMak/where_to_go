# Generated by Django 5.0 on 2023-12-12 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.place', verbose_name='Место с картинки')),
            ],
        ),
    ]