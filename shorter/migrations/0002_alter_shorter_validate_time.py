# Generated by Django 3.2.7 on 2021-10-04 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorter',
            name='validate_time',
            field=models.PositiveIntegerField(default=60, validators=[django.core.validators.MaxValueValidator(1440)]),
        ),
    ]
