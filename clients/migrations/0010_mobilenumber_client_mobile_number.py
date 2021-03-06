# Generated by Django 4.0 on 2021-12-23 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_remove_client_mobile_number_delete_mobilenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Enter phone number.', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='mobile_number',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='clients.mobilenumber'),
            preserve_default=False,
        ),
    ]
