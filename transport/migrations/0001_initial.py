# Generated by Django 4.1.5 on 2023-01-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('service_interval', models.IntegerField()),
                ('next_service', models.DateField()),
                ('length', models.DecimalField(decimal_places=2, max_digits=9)),
                ('width', models.DecimalField(decimal_places=2, max_digits=6)),
                ('NIH', models.CharField(max_length=200)),
                ('current_hours', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('service_interval', models.IntegerField()),
                ('next_service', models.DateField()),
                ('seats', models.IntegerField()),
                ('color', models.CharField(max_length=200)),
                ('VIN', models.CharField(max_length=200)),
                ('current_mileage', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('service_interval', models.IntegerField()),
                ('next_service', models.DateField()),
                ('seats', models.IntegerField()),
                ('color', models.CharField(max_length=200)),
                ('bed_length', models.DecimalField(decimal_places=2, max_digits=6)),
                ('VIN', models.CharField(max_length=200)),
                ('current_mileage', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]