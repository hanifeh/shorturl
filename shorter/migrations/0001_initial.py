# Generated by Django 3.2.7 on 2021-10-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shorter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('short_url', models.CharField(max_length=15, unique=True)),
                ('counter', models.PositiveIntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('validate_time', models.PositiveIntegerField(default=60)),
                ('expire_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('public', 'Public'), ('privet', 'Privet')], default='public', max_length=15)),
                ('one_time_password', models.CharField(max_length=12)),
            ],
        ),
    ]
