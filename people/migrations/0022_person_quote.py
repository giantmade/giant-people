# Generated by Django 2.2 on 2022-07-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0021_add_container_plugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='quote',
            field=models.TextField(blank=True, help_text='Optional. A single paragraph. Quotation marks need to be added if intended'),
        ),
    ]
