# Generated by Django 4.0.2 on 2023-12-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0004_remove_parkingspot_parking_center_customuser_center_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
