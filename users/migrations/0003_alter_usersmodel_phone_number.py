# Generated by Django 4.2.13 on 2024-06-23 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usersmodel_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
