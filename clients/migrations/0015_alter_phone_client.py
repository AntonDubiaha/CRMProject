# Generated by Django 4.0 on 2022-01-07 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_alter_client_company_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_phones', to='clients.client'),
        ),
    ]
