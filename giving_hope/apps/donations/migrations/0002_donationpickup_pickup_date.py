# Generated by Django 3.2.8 on 2021-12-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationpickup',
            name='pickup_date',
            field=models.DateTimeField(null=True),
        ),
    ]