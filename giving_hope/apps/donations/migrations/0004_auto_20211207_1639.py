# Generated by Django 3.2.8 on 2021-12-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_auto_20211207_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationpickup',
            name='pickup_time',
        ),
        migrations.AlterField(
            model_name='donationpickup',
            name='pickup_date',
            field=models.DateTimeField(null=True),
        ),
    ]
