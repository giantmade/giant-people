# Generated by Django 2.2.10 on 2020-02-19 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_person_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name'], 'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
    ]
