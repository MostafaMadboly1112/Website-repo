# Generated by Django 5.0.3 on 2024-03-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avs', models.CharField(default='', max_length=16, unique=True)),
                ('user', models.CharField(max_length=30, unique=True)),
                ('booking_from', models.DateTimeField()),
                ('booking_to', models.DateTimeField()),
                ('Tec_data', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
