# Generated by Django 3.2.10 on 2023-08-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default='닉네임', max_length=20, null=True),
        ),
    ]