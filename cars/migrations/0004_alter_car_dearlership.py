# Generated by Django 4.2.1 on 2023-05-16 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealerships', '0001_initial'),
        ('cars', '0003_car_dearlership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='dearlership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dealerships.dealerships'),
            preserve_default=False,
        ),
    ]
