# Generated by Django 3.2.7 on 2021-10-23 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committee',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='historicalcommittee',
            name='is_approved',
        ),
    ]
