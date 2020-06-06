# Generated by Django 2.1.5 on 2020-04-03 20:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_commentreport_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='value',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]