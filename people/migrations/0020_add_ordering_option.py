# Generated by Django 2.2 on 2021-01-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0019_strip_classes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-order', 'name'], 'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='person',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Set this to prioritise the order of the person, higher numbers are higher priority'),
        ),
    ]
