# Generated by Django 4.2.1 on 2023-05-17 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_dearlership'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='dearlership',
            new_name='dealership',
        ),
    ]
