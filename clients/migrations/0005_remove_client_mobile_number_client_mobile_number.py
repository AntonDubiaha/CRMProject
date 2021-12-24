# Generated by Django 4.0 on 2021-12-23 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_remove_client_email_client_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='mobile_number',
        ),
        migrations.AddField(
            model_name='client',
            name='mobile_number',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='clients.mobilenumber'),
            preserve_default=False,
        ),
    ]
