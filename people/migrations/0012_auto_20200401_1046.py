# Generated by Django 2.2.11 on 2020-04-01 10:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20200311_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='linkedin_url',
            field=models.URLField(blank=True, help_text='Enter the full URL of the LinkedIn page', validators=[django.core.validators.URLValidator(message='Please enter the full URL of the LinkedIn page', regex='www.linkedin.com', schemes=['https'])]),
        ),
    ]