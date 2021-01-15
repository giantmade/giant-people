# Generated by Django 2.2.10 on 2020-02-19 09:49

import mixins.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20191219_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', mixins.fields.AutoDateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(choices=[('location_one', 'Location One'), ('location_two', 'Location Two')], max_length=255)),
                ('department', models.CharField(choices=[('department_one', 'Department One'), ('department_two', 'Department Two')], max_length=255)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', mixins.fields.AutoDateTimeField(default=django.utils.timezone.now)),
                ('role_id', models.CharField(max_length=256)),
                ('role', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['tag'],
            },
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='department',
        ),
        migrations.RemoveField(
            model_name='person',
            name='location',
        ),
        migrations.RemoveField(
            model_name='person',
            name='role',
        ),
        migrations.RemoveField(
            model_name='person',
            name='tags',
        ),
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='person',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Selecting this option will publish this item'),
        ),
        migrations.AddField(
            model_name='person',
            name='publish_at',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='updated_at',
            field=mixins.fields.AutoDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.AddField(
            model_name='role',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='people.Person'),
        ),
        migrations.AddField(
            model_name='location',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='people.Person'),
        ),
    ]
