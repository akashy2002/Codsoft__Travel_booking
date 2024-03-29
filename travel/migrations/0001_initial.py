# Generated by Django 4.1.7 on 2023-07-21 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('upadate_at', models.DateField(auto_now_add=True)),
                ('flight_name', models.CharField(max_length=100)),
                ('flight_price', models.IntegerField()),
                ('description', models.TextField()),
                ('pasanger_count', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Flightbooking',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('upadate_at', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('booking_type', models.CharField(choices=[('Pre paid', 'Pre paid'), ('Post paid', 'Post Paid')], max_length=100)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_booking', to='travel.flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
