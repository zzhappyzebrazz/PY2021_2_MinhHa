# Generated by Django 4.1.2 on 2022-11-12 04:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catergory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('author', models.CharField(max_length=250)),
                ('url', models.URLField(null=True)),
                ('content', models.TextField()),
                ('public_day', models.DateTimeField(default=datetime.date.today)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stories.catergory')),
            ],
        ),
    ]
