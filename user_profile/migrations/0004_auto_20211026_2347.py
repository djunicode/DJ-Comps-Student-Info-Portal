# Generated by Django 3.2.7 on 2021-10-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20211026_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalinternship',
            name='Loc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='internship',
            name='Loc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]