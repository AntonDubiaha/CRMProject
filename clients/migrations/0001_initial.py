# Generated by Django 4.0 on 2021-12-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namecompany', models.CharField(max_length=200)),
                ('fullnameuser', models.CharField(max_length=100)),
                ('companydesc', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=200)),
                ('number', models.SlugField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
