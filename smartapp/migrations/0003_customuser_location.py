# Generated by Django 4.0.2 on 2023-12-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0002_parkingspot_location_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.CharField(default=3212, max_length=100),
            preserve_default=False,
        ),
    ]
