# Generated by Django 3.2.7 on 2021-10-05 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0002_alter_shorter_validate_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorter',
            name='expire_time',
        ),
    ]