# Generated by Django 4.1.7 on 2023-07-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightbooking',
            name='booking_type',
            field=models.BooleanField(choices=[('Success', 'Success'), ('Failed', 'Failed')], max_length=100),
        ),
    ]
