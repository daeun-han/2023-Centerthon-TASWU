# Generated by Django 3.2.10 on 2023-07-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_taxi_driver',
            field=models.BooleanField(default=False),
        ),
    ]