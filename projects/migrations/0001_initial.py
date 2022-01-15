# Generated by Django 4.0 on 2022-01-11 16:52

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0016_alter_phone_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', tinymce.models.HTMLField()),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_project', to='clients.client')),
            ],
        ),
    ]